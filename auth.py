"""
Authentication utilities for the OpenBankProject API Client.
"""

import base64
import json
import time
from typing import Dict, Optional


class DirectLoginAuth:
    """
    Authentication handler for DirectLogin authentication method.
    """
    
    def __init__(self, username: Optional[str] = None, password: Optional[str] = None, 
                 consumer_key: Optional[str] = None, token: Optional[str] = None):
        """
        Initialize DirectLogin authentication.
        
        Args:
            username: User's username (required if token not provided)
            password: User's password (required if token not provided)
            consumer_key: Consumer key for the application (required if token not provided)
            token: Pre-generated DirectLogin token (optional)
        """
        self.username = username
        self.password = password
        self.consumer_key = consumer_key
        self.token = token
        
        if not token and not (username and password and consumer_key):
            raise ValueError("Either token or (username, password, consumer_key) must be provided")
    
    def get_headers(self) -> Dict[str, str]:
        """
        Get authentication headers.
        
        Returns:
            Dict containing the Authorization header
        """
        if self.token:
            return {"Authorization": f"DirectLogin token={self.token}"}
        else:
            auth_string = f'DirectLogin username="{self.username}", password="{self.password}", consumer_key="{self.consumer_key}"'
            return {"Authorization": auth_string}
    
    def authenticate(self, client) -> bool:
        """
        Authenticate with the API and get a token if needed.
        
        Args:
            client: OpenBankProjectClient instance
            
        Returns:
            True if authentication was successful
        """
        if self.token:
            # Already have a token, no need to authenticate
            return True
        
        try:
            # Make a request to get a token
            # This is a placeholder - the actual endpoint may vary
            response = client.request(
                'GET', 
                'my/logins/direct', 
                headers=self.get_headers()
            )
            
            if 'token' in response:
                self.token = response['token']
                return True
            return False
        except Exception:
            return False


class GatewayLoginAuth:
    """
    Authentication handler for GatewayLogin authentication method.
    """
    
    def __init__(self, token: str):
        """
        Initialize GatewayLogin authentication.
        
        Args:
            token: GatewayLogin JWT token
        """
        self.token = token
    
    def get_headers(self) -> Dict[str, str]:
        """
        Get authentication headers.
        
        Returns:
            Dict containing the Authorization header
        """
        return {"Authorization": f"GatewayLogin token={self.token}"}
    
    def authenticate(self, client) -> bool:
        """
        Authenticate with the API.
        
        Args:
            client: OpenBankProjectClient instance
            
        Returns:
            True if authentication was successful
        """
        # GatewayLogin uses a pre-generated token, so no authentication request is needed
        return True


class Authentication:
    """Authentication utilities for the OpenBankProject API."""
    
    @staticmethod
    def create_direct_login_header(username: str, password: str, consumer_key: str) -> Dict[str, str]:
        """
        Create a DirectLogin authorization header.
        
        Args:
            username: User's username
            password: User's password
            consumer_key: Consumer key for the application
            
        Returns:
            Dict containing the Authorization header
        """
        auth_string = f'DirectLogin username="{username}", password="{password}", consumer_key="{consumer_key}"'
        return {"Authorization": auth_string}
    
    @staticmethod
    def create_gateway_login_header(jwt: str) -> Dict[str, str]:
        """
        Create a GatewayLogin authorization header.
        
        Args:
            jwt: JSON Web Token for authentication
            
        Returns:
            Dict containing the Authorization header
        """
        return {"Authorization": f"GatewayLogin token={jwt}"}
    
    @staticmethod
    def create_token_header(token: str, auth_type: str = "DirectLogin") -> Dict[str, str]:
        """
        Create an authorization header using a token.
        
        Args:
            token: Authentication token
            auth_type: Authentication type (DirectLogin or GatewayLogin)
            
        Returns:
            Dict containing the Authorization header
        """
        if auth_type not in ["DirectLogin", "GatewayLogin"]:
            raise ValueError("auth_type must be either 'DirectLogin' or 'GatewayLogin'")
        
        return {"Authorization": f"{auth_type} token={token}"}
    
    @staticmethod
    def generate_jwt(consumer_key: str, 
                     consumer_secret: str, 
                     user_id: Optional[str] = None, 
                     expiry_seconds: int = 3600) -> str:
        """
        Generate a JWT token for GatewayLogin.
        
        This is a simplified implementation and may need to be adjusted based on
        the specific requirements of the OpenBankProject API.
        
        Args:
            consumer_key: Consumer key for the application
            consumer_secret: Consumer secret for the application
            user_id: Optional user ID to include in the token
            expiry_seconds: Token expiry time in seconds (default: 1 hour)
            
        Returns:
            JWT token string
        """
        # Create header
        header = {
            "alg": "HS256",
            "typ": "JWT"
        }
        
        # Create payload
        now = int(time.time())
        payload = {
            "iss": consumer_key,
            "iat": now,
            "exp": now + expiry_seconds
        }
        
        if user_id:
            payload["sub"] = user_id
        
        # Encode header and payload
        header_encoded = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip('=')
        payload_encoded = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip('=')
        
        # Create signature
        import hmac
        import hashlib
        
        signature_data = f"{header_encoded}.{payload_encoded}"
        signature = hmac.new(
            consumer_secret.encode(),
            signature_data.encode(),
            hashlib.sha256
        ).digest()
        
        signature_encoded = base64.urlsafe_b64encode(signature).decode().rstrip('=')
        
        # Combine to create JWT
        return f"{header_encoded}.{payload_encoded}.{signature_encoded}"

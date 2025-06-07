"""
Role endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class RoleEndpoints:
    """Role-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def add_entitlement_for_user(self, bank_id: str, user_id: str, role_name: str) -> Dict:
        """
        Add Entitlement for a User.
        
        Args:
            bank_id: Bank identifier
            user_id: User identifier
            role_name: Role name
            
        Returns:
            Dict containing entitlement information
        """
        return self.client.post(f"banks/{bank_id}/users/{user_id}/entitlements/{role_name}", data={})
    
    def create_user_with_roles(self, bank_id: str, data: Dict) -> Dict:
        """
        Create (DAuth) User with Roles.
        
        Args:
            bank_id: Bank identifier
            data: User and roles data
            
        Returns:
            Dict containing created user information
        """
        return self.client.post(f"banks/{bank_id}/user-entitlements", data=data)
    
    def create_entitlement_request_for_current_user(self, bank_id: str, data: Dict) -> Dict:
        """
        Create Entitlement Request for current User.
        
        Args:
            bank_id: Bank identifier
            data: Entitlement request data
            
        Returns:
            Dict containing created entitlement request information
        """
        return self.client.post(f"banks/{bank_id}/entitlement-requests", data=data)
    
    def delete_entitlement(self, bank_id: str, user_id: str, role_name: str) -> Dict:
        """
        Delete Entitlement.
        
        Args:
            bank_id: Bank identifier
            user_id: User identifier
            role_name: Role name
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/users/{user_id}/entitlements/{role_name}")
    
    def delete_entitlement_request(self, entitlement_request_id: str) -> Dict:
        """
        Delete Entitlement Request.
        
        Args:
            entitlement_request_id: Entitlement request identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"entitlement-requests/{entitlement_request_id}")
    
    def get_entitlement_requests_for_user(self, user_id: str) -> Dict:
        """
        Get Entitlement Requests for a User.
        
        Args:
            user_id: User identifier
            
        Returns:
            Dict containing entitlement requests information
        """
        return self.client.get(f"users/{user_id}/entitlement-requests")
    
    def get_entitlement_requests_for_current_user(self) -> Dict:
        """
        Get Entitlement Requests for the current User.
        
        Returns:
            Dict containing entitlement requests information
        """
        return self.client.get("my/entitlement-requests")
    
    def get_entitlements_and_permissions_for_user(self, user_id: str) -> Dict:
        """
        Get Entitlements and Permissions for a User.
        
        Args:
            user_id: User identifier
            
        Returns:
            Dict containing entitlements and permissions information
        """
        return self.client.get(f"users/{user_id}/entitlements/permissions")
    
    def get_entitlements_for_one_bank(self, bank_id: str) -> Dict:
        """
        Get Entitlements for One Bank.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing entitlements information
        """
        return self.client.get(f"banks/{bank_id}/entitlements")
    
    def get_entitlements_for_user(self, user_id: str) -> Dict:
        """
        Get Entitlements for User.
        
        Args:
            user_id: User identifier
            
        Returns:
            Dict containing entitlements information
        """
        return self.client.get(f"users/{user_id}/entitlements")
    
    def get_entitlements_for_user_at_bank(self, bank_id: str, user_id: str) -> Dict:
        """
        Get Entitlements for User at Bank.
        
        Args:
            bank_id: Bank identifier
            user_id: User identifier
            
        Returns:
            Dict containing entitlements information
        """
        return self.client.get(f"banks/{bank_id}/users/{user_id}/entitlements")
    
    def get_entitlements_for_current_user(self) -> Dict:
        """
        Get Entitlements for the current User.
        
        Returns:
            Dict containing entitlements information
        """
        return self.client.get("my/entitlements")
    
    def get_roles(self) -> Dict:
        """
        Get Roles.
        
        Returns:
            Dict containing roles information
        """
        return self.client.get("roles")
    
    def get_all_entitlement_requests(self) -> Dict:
        """
        Get all Entitlement Requests.
        
        Returns:
            Dict containing all entitlement requests information
        """
        return self.client.get("entitlement-requests")
    
    def get_all_entitlements(self) -> Dict:
        """
        Get all Entitlements.
        
        Returns:
            Dict containing all entitlements information
        """
        return self.client.get("entitlements")

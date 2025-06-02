"""
OpenBankProject API Client

This module provides a comprehensive client for interacting with the OpenBankProject API v5.1.0.
It includes support for all API endpoints, authentication methods, and error handling.
"""

import json
import requests
from typing import Dict, List, Optional, Union, Any

from .auth import DirectLoginAuth, GatewayLoginAuth
from .errors import (
    ApiError, AuthenticationError, ResourceNotFoundError, 
    ValidationError, PermissionError, ServerError
)

# Import all endpoint modules
from .account_access import AccountAccessEndpoints
from .account_application import AccountApplicationEndpoints
from .account_holder import AccountHolderEndpoints
from .account_metadata import AccountMetadataEndpoints
from .account_public import AccountPublicEndpoints
from .api_collection import ApiCollectionEndpoints
from .api_configuration import ApiConfigurationEndpoints
from .api_favorite import ApiFavoriteEndpoints
from .api_management import ApiManagementEndpoints
from .atm import AtmEndpoints
from .branch import BranchEndpoints
from .card import CardEndpoints
from .connector_method import ConnectorMethodEndpoints
from .consent import ConsentEndpoints
from .counterparty import CounterpartyEndpoints
from .counterparty_limits import CounterpartyLimitsEndpoints
from .counterparty_metadata import CounterpartyMetadataEndpoints
from .customer import CustomerEndpoints
from .customer_meeting import CustomerMeetingEndpoints
from .customer_message import CustomerMessageEndpoints
from .direct_debit import DirectDebitEndpoints
from .dynamic_endpoint import DynamicEndpointEndpoints
from .dynamic_entity import DynamicEntityEndpoints
from .dynamic_message_doc import DynamicMessageDocEndpoints
from .dynamic_resource_doc import DynamicResourceDocEndpoints
from .extended_account import ExtendedAccountEndpoints
from .extended_bank import ExtendedBankEndpoints
from .fx import FxEndpoints
from .kyc import KycEndpoints
from .metric import MetricEndpoints
from .product import ProductEndpoints
from .role import RoleEndpoints
from .scheduled_event import ScheduledEventEndpoints
from .scope import ScopeEndpoints
from .standing_order import StandingOrderEndpoints
from .transaction import TransactionEndpoints
from .transaction_metadata import TransactionMetadataEndpoints
from .transaction_request import TransactionRequestEndpoints
from .user import UserEndpoints
from .user_invitation import UserInvitationEndpoints
from .view_custom import ViewCustomEndpoints
from .view_system import ViewSystemEndpoints
from .webhook import WebhookEndpoints
from .webui_props import WebUiPropsEndpoints


class OpenBankProjectClient:
    """
    Client for the OpenBankProject API.
    
    This client provides access to all API endpoints and handles authentication,
    request formatting, and error handling.
    """
    
    def __init__(
        self, 
        base_url: str = "https://api.openbankproject.com",
        api_version: str = "v5.1.0",
        direct_login_token: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        consumer_key: Optional[str] = None,
        gateway_login_token: Optional[str] = None,
        timeout: int = 30
    ):
        """
        Initialize the OpenBankProject API client.
        
        Args:
            base_url: Base URL of the API server
            api_version: API version to use
            direct_login_token: Pre-generated DirectLogin token (if available)
            username: Username for DirectLogin authentication
            password: Password for DirectLogin authentication
            consumer_key: Consumer key for DirectLogin authentication
            gateway_login_token: Pre-generated GatewayLogin token (if available)
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip('/')
        self.api_version = api_version
        self.timeout = timeout
        self.session = requests.Session()
        
        # Set up authentication
        self.auth = None
        if direct_login_token:
            self.auth = DirectLoginAuth(token=direct_login_token)
        elif username and password and consumer_key:
            self.auth = DirectLoginAuth(
                username=username,
                password=password,
                consumer_key=consumer_key
            )
        elif gateway_login_token:
            self.auth = GatewayLoginAuth(token=gateway_login_token)
            
        # Initialize endpoint groups
        self.account_access = AccountAccessEndpoints(self)
        self.account_application = AccountApplicationEndpoints(self)
        self.account_holder = AccountHolderEndpoints(self)
        self.account_metadata = AccountMetadataEndpoints(self)
        self.account_public = AccountPublicEndpoints(self)
        self.api_collection = ApiCollectionEndpoints(self)
        self.api_configuration = ApiConfigurationEndpoints(self)
        self.api_favorite = ApiFavoriteEndpoints(self)
        self.api_management = ApiManagementEndpoints(self)
        self.atm = AtmEndpoints(self)
        self.branch = BranchEndpoints(self)
        self.card = CardEndpoints(self)
        self.connector_method = ConnectorMethodEndpoints(self)
        self.consent = ConsentEndpoints(self)
        self.counterparty = CounterpartyEndpoints(self)
        self.counterparty_limits = CounterpartyLimitsEndpoints(self)
        self.counterparty_metadata = CounterpartyMetadataEndpoints(self)
        self.customer = CustomerEndpoints(self)
        self.customer_meeting = CustomerMeetingEndpoints(self)
        self.customer_message = CustomerMessageEndpoints(self)
        self.direct_debit = DirectDebitEndpoints(self)
        self.dynamic_endpoint = DynamicEndpointEndpoints(self)
        self.dynamic_entity = DynamicEntityEndpoints(self)
        self.dynamic_message_doc = DynamicMessageDocEndpoints(self)
        self.dynamic_resource_doc = DynamicResourceDocEndpoints(self)
        self.extended_account = ExtendedAccountEndpoints(self)
        self.extended_bank = ExtendedBankEndpoints(self)
        self.fx = FxEndpoints(self)
        self.kyc = KycEndpoints(self)
        self.metric = MetricEndpoints(self)
        self.product = ProductEndpoints(self)
        self.role = RoleEndpoints(self)
        self.scheduled_event = ScheduledEventEndpoints(self)
        self.scope = ScopeEndpoints(self)
        self.standing_order = StandingOrderEndpoints(self)
        self.transaction = TransactionEndpoints(self)
        self.transaction_metadata = TransactionMetadataEndpoints(self)
        self.transaction_request = TransactionRequestEndpoints(self)
        self.user = UserEndpoints(self)
        self.user_invitation = UserInvitationEndpoints(self)
        self.view_custom = ViewCustomEndpoints(self)
        self.view_system = ViewSystemEndpoints(self)
        self.webhook = WebhookEndpoints(self)
        self.webui_props = WebUiPropsEndpoints(self)
    
    def _build_url(self, endpoint: str) -> str:
        """
        Build a full URL for the given endpoint.
        
        Args:
            endpoint: API endpoint path
            
        Returns:
            Full URL including base URL and API version
        """
        # Remove leading slash if present
        endpoint = endpoint.lstrip('/')
        return f"{self.base_url}/{self.api_version}/{endpoint}"
    
    def _handle_response(self, response: requests.Response) -> Dict:
        """
        Handle API response and raise appropriate exceptions for errors.
        
        Args:
            response: Response object from requests
            
        Returns:
            Parsed JSON response as dictionary
            
        Raises:
            AuthenticationError: For authentication issues (401)
            PermissionError: For permission issues (403)
            ResourceNotFoundError: When resource is not found (404)
            ValidationError: For validation errors (400)
            ServerError: For server errors (5xx)
            ApiError: For other API errors
        """
        try:
            response_json = response.json()
        except ValueError:
            response_json = {"message": response.text}
            
        if response.status_code >= 200 and response.status_code < 300:
            return response_json
            
        error_msg = response_json.get('message', response.text)
        
        if response.status_code == 401:
            raise AuthenticationError(error_msg, response.status_code, response_json)
        elif response.status_code == 403:
            raise PermissionError(error_msg, response.status_code, response_json)
        elif response.status_code == 404:
            raise ResourceNotFoundError(error_msg, response.status_code, response_json)
        elif response.status_code == 400:
            raise ValidationError(error_msg, response.status_code, response_json)
        elif response.status_code >= 500:
            raise ServerError(error_msg, response.status_code, response_json)
        else:
            raise ApiError(error_msg, response.status_code, response_json)
    
    def request(self, method: str, endpoint: str, **kwargs) -> Dict:
        """
        Make a request to the API.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint path
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Parsed JSON response as dictionary
            
        Raises:
            Various exceptions based on API response
        """
        url = self._build_url(endpoint)
        
        # Add authentication headers if available
        headers = kwargs.pop('headers', {})
        if self.auth:
            auth_headers = self.auth.get_headers()
            headers.update(auth_headers)
            
        # Set default content type for requests with body
        if method.upper() in ['POST', 'PUT', 'PATCH'] and 'data' in kwargs:
            if 'content-type' not in {k.lower(): v for k, v in headers.items()}:
                headers['Content-Type'] = 'application/json'
                
            # Convert data to JSON if it's a dict
            if isinstance(kwargs['data'], dict):
                kwargs['data'] = json.dumps(kwargs['data'])
                
        kwargs['headers'] = headers
        kwargs['timeout'] = kwargs.get('timeout', self.timeout)
        
        response = self.session.request(method, url, **kwargs)
        return self._handle_response(response)
    
    def get(self, endpoint: str, **kwargs) -> Dict:
        """
        Make a GET request to the API.
        
        Args:
            endpoint: API endpoint path
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Parsed JSON response as dictionary
        """
        return self.request('GET', endpoint, **kwargs)
    
    def post(self, endpoint: str, **kwargs) -> Dict:
        """
        Make a POST request to the API.
        
        Args:
            endpoint: API endpoint path
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Parsed JSON response as dictionary
        """
        return self.request('POST', endpoint, **kwargs)
    
    def put(self, endpoint: str, **kwargs) -> Dict:
        """
        Make a PUT request to the API.
        
        Args:
            endpoint: API endpoint path
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Parsed JSON response as dictionary
        """
        return self.request('PUT', endpoint, **kwargs)
    
    def delete(self, endpoint: str, **kwargs) -> Dict:
        """
        Make a DELETE request to the API.
        
        Args:
            endpoint: API endpoint path
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Parsed JSON response as dictionary
        """
        return self.request('DELETE', endpoint, **kwargs)
    
    def authenticate(self) -> bool:
        """
        Authenticate with the API if not already authenticated.
        
        Returns:
            True if authentication was successful
            
        Raises:
            AuthenticationError: If authentication fails
        """
        if self.auth:
            return self.auth.authenticate(self)
        return False

"""
API Management endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class ApiManagementEndpoints:
    """API Management-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_bank_level_endpoint_tag(self, bank_id: str, data: Dict) -> Dict:
        """
        Create a bank level endpoint tag.
        
        Args:
            bank_id: Bank identifier
            data: Endpoint tag data
            
        Returns:
            Dict containing created endpoint tag information
        """
        return self.client.post(f"management/banks/{bank_id}/endpoints/tags", data=data)
    
    def create_system_level_endpoint_tag(self, data: Dict) -> Dict:
        """
        Create a system level endpoint tag.
        
        Args:
            data: Endpoint tag data
            
        Returns:
            Dict containing created endpoint tag information
        """
        return self.client.post("management/endpoints/tags", data=data)
    
    def delete_bank_level_endpoint_tag(self, bank_id: str, tag_id: str) -> Dict:
        """
        Delete a bank level endpoint tag.
        
        Args:
            bank_id: Bank identifier
            tag_id: Tag identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"management/banks/{bank_id}/endpoints/tags/{tag_id}")
    
    def delete_system_level_endpoint_tag(self, tag_id: str) -> Dict:
        """
        Delete a system level endpoint tag.
        
        Args:
            tag_id: Tag identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"management/endpoints/tags/{tag_id}")
    
    def get_api_configuration(self) -> Dict:
        """
        Get API configuration.
        
        Returns:
            Dict containing API configuration information
        """
        return self.client.get("config")
    
    def get_api_info(self) -> Dict:
        """
        Get API info (root).
        
        Returns:
            Dict containing API information
        """
        return self.client.get("")
    
    def get_api_tags(self) -> Dict:
        """
        Get API tags.
        
        Returns:
            Dict containing API tag information
        """
        return self.client.get("api/tags")
    
    def get_adapter_info_for_bank(self, bank_id: str) -> Dict:
        """
        Get adapter info for a bank.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing adapter information for the bank
        """
        return self.client.get(f"banks/{bank_id}/adapter")
    
    def get_bank_level_endpoint_tags(self, bank_id: str) -> Dict:
        """
        Get bank level endpoint tags.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing bank level endpoint tag information
        """
        return self.client.get(f"management/banks/{bank_id}/endpoints/tags")
    
    def get_connector_status(self) -> Dict:
        """
        Get connector status (Loopback).
        
        Returns:
            Dict containing connector status information
        """
        return self.client.get("connector/status")
    
    def get_json_web_key(self) -> Dict:
        """
        Get JSON Web Key (JWK).
        
        Returns:
            Dict containing JWK information
        """
        return self.client.get("jwk")
    
    def get_json_web_key_uris(self) -> Dict:
        """
        Get JSON Web Key (JWK) URIs.
        
        Returns:
            Dict containing JWK URI information
        """
        return self.client.get("jwk/uris")
    
    def get_mapper_database_info(self) -> Dict:
        """
        Get mapper database info.
        
        Returns:
            Dict containing mapper database information
        """
        return self.client.get("database/info")
    
    def get_rate_limiting_info(self) -> Dict:
        """
        Get rate limiting info.
        
        Returns:
            Dict containing rate limiting information
        """
        return self.client.get("rate-limiting")
    
    def get_suggested_session_timeout(self) -> Dict:
        """
        Get suggested session timeout.
        
        Returns:
            Dict containing suggested session timeout information
        """
        return self.client.get("session/timeout")
    
    def get_system_level_endpoint_tags(self) -> Dict:
        """
        Get system level endpoint tags.
        
        Returns:
            Dict containing system level endpoint tag information
        """
        return self.client.get("management/endpoints/tags")
    
    def get_call_context(self) -> Dict:
        """
        Get the call context of a current call.
        
        Returns:
            Dict containing call context information
        """
        return self.client.get("call-context")
    
    def update_bank_level_endpoint_tag(self, bank_id: str, tag_id: str, data: Dict) -> Dict:
        """
        Update a bank level endpoint tag.
        
        Args:
            bank_id: Bank identifier
            tag_id: Tag identifier
            data: Updated endpoint tag data
            
        Returns:
            Dict containing updated endpoint tag information
        """
        return self.client.put(f"management/banks/{bank_id}/endpoints/tags/{tag_id}", data=data)
    
    def update_system_level_endpoint_tag(self, tag_id: str, data: Dict) -> Dict:
        """
        Update a system level endpoint tag.
        
        Args:
            tag_id: Tag identifier
            data: Updated endpoint tag data
            
        Returns:
            Dict containing updated endpoint tag information
        """
        return self.client.put(f"management/endpoints/tags/{tag_id}", data=data)
    
    def verify_request_and_sign_response(self, data: Dict) -> Dict:
        """
        Verify request and sign response of a current call.
        
        Args:
            data: Verification data
            
        Returns:
            Dict containing verification and signature information
        """
        return self.client.post("verify", data=data)

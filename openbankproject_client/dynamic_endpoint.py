"""
Dynamic Endpoint endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class DynamicEndpointEndpoints:
    """Dynamic Endpoint-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_dynamic_endpoint(self, data: Dict) -> Dict:
        """
        Create Dynamic Endpoint.
        
        Args:
            data: Dynamic endpoint data
            
        Returns:
            Dict containing created dynamic endpoint information
        """
        return self.client.post("management/dynamic-endpoints", data=data)
    
    def get_dynamic_endpoint(self, dynamic_endpoint_id: str) -> Dict:
        """
        Get Dynamic Endpoint.
        
        Args:
            dynamic_endpoint_id: Dynamic endpoint identifier
            
        Returns:
            Dict containing dynamic endpoint information
        """
        return self.client.get(f"management/dynamic-endpoints/{dynamic_endpoint_id}")
    
    def get_dynamic_endpoints(self) -> Dict:
        """
        Get Dynamic Endpoints.
        
        Returns:
            Dict containing dynamic endpoints information
        """
        return self.client.get("management/dynamic-endpoints")
    
    def update_dynamic_endpoint(self, dynamic_endpoint_id: str, data: Dict) -> Dict:
        """
        Update Dynamic Endpoint.
        
        Args:
            dynamic_endpoint_id: Dynamic endpoint identifier
            data: Updated dynamic endpoint data
            
        Returns:
            Dict containing updated dynamic endpoint information
        """
        return self.client.put(f"management/dynamic-endpoints/{dynamic_endpoint_id}", data=data)
    
    def delete_dynamic_endpoint(self, dynamic_endpoint_id: str) -> Dict:
        """
        Delete Dynamic Endpoint.
        
        Args:
            dynamic_endpoint_id: Dynamic endpoint identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"management/dynamic-endpoints/{dynamic_endpoint_id}")

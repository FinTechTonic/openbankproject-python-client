"""
Connector Method endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class ConnectorMethodEndpoints:
    """Connector Method-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_connector_method(self, data: Dict) -> Dict:
        """
        Create Connector Method.
        
        Args:
            data: Connector method data
            
        Returns:
            Dict containing created connector method information
        """
        return self.client.post("management/connector-methods", data=data)
    
    def get_connector_method(self, connector_method_id: str) -> Dict:
        """
        Get Connector Method.
        
        Args:
            connector_method_id: Connector method identifier
            
        Returns:
            Dict containing connector method information
        """
        return self.client.get(f"management/connector-methods/{connector_method_id}")
    
    def get_connector_methods(self) -> Dict:
        """
        Get Connector Methods.
        
        Returns:
            Dict containing connector methods information
        """
        return self.client.get("management/connector-methods")
    
    def update_connector_method(self, connector_method_id: str, data: Dict) -> Dict:
        """
        Update Connector Method.
        
        Args:
            connector_method_id: Connector method identifier
            data: Updated connector method data
            
        Returns:
            Dict containing updated connector method information
        """
        return self.client.put(f"management/connector-methods/{connector_method_id}", data=data)
    
    def delete_connector_method(self, connector_method_id: str) -> Dict:
        """
        Delete Connector Method.
        
        Args:
            connector_method_id: Connector method identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"management/connector-methods/{connector_method_id}")

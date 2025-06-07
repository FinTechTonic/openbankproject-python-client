"""
API Collection endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class ApiCollectionEndpoints:
    """API Collection-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_api_collection(self, data: Dict) -> Dict:
        """
        Create API Collection.
        
        Args:
            data: API collection data
            
        Returns:
            Dict containing created API collection information
        """
        return self.client.post("api-collections", data=data)
    
    def get_api_collection(self, collection_id: str) -> Dict:
        """
        Get API Collection.
        
        Args:
            collection_id: Collection identifier
            
        Returns:
            Dict containing API collection information
        """
        return self.client.get(f"api-collections/{collection_id}")
    
    def get_api_collections(self) -> Dict:
        """
        Get API Collections.
        
        Returns:
            Dict containing API collections information
        """
        return self.client.get("api-collections")
    
    def update_api_collection(self, collection_id: str, data: Dict) -> Dict:
        """
        Update API Collection.
        
        Args:
            collection_id: Collection identifier
            data: Updated API collection data
            
        Returns:
            Dict containing updated API collection information
        """
        return self.client.put(f"api-collections/{collection_id}", data=data)
    
    def delete_api_collection(self, collection_id: str) -> Dict:
        """
        Delete API Collection.
        
        Args:
            collection_id: Collection identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"api-collections/{collection_id}")

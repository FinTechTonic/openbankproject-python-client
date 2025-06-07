"""
API Favorite endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class ApiFavoriteEndpoints:
    """API Favorite-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_api_favorite(self, data: Dict) -> Dict:
        """
        Create API Favorite.
        
        Args:
            data: API favorite data
            
        Returns:
            Dict containing created API favorite information
        """
        return self.client.post("api-favorites", data=data)
    
    def get_api_favorite(self, favorite_id: str) -> Dict:
        """
        Get API Favorite.
        
        Args:
            favorite_id: Favorite identifier
            
        Returns:
            Dict containing API favorite information
        """
        return self.client.get(f"api-favorites/{favorite_id}")
    
    def get_api_favorites(self) -> Dict:
        """
        Get API Favorites.
        
        Returns:
            Dict containing API favorites information
        """
        return self.client.get("api-favorites")
    
    def update_api_favorite(self, favorite_id: str, data: Dict) -> Dict:
        """
        Update API Favorite.
        
        Args:
            favorite_id: Favorite identifier
            data: Updated API favorite data
            
        Returns:
            Dict containing updated API favorite information
        """
        return self.client.put(f"api-favorites/{favorite_id}", data=data)
    
    def delete_api_favorite(self, favorite_id: str) -> Dict:
        """
        Delete API Favorite.
        
        Args:
            favorite_id: Favorite identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"api-favorites/{favorite_id}")

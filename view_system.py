"""
View System endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class ViewSystemEndpoints:
    """View System-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_system_view(self, data: Dict) -> Dict:
        """
        Create System View.
        
        Args:
            data: System view data
            
        Returns:
            Dict containing created system view information
        """
        return self.client.post("system-views", data=data)
    
    def get_system_view(self, view_id: str) -> Dict:
        """
        Get System View.
        
        Args:
            view_id: View identifier
            
        Returns:
            Dict containing system view information
        """
        return self.client.get(f"system-views/{view_id}")
    
    def get_ids_of_system_views(self) -> Dict:
        """
        Get Ids of System Views.
        
        Returns:
            Dict containing system view IDs
        """
        return self.client.get("system-views")
    
    def update_system_view(self, view_id: str, data: Dict) -> Dict:
        """
        Update System View.
        
        Args:
            view_id: View identifier
            data: Updated system view data
            
        Returns:
            Dict containing updated system view information
        """
        return self.client.put(f"system-views/{view_id}", data=data)
    
    def delete_system_view(self, view_id: str) -> Dict:
        """
        Delete System View.
        
        Args:
            view_id: View identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"system-views/{view_id}")

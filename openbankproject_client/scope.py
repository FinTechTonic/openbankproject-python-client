"""
Scope endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class ScopeEndpoints:
    """Scope-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def get_scopes(self) -> Dict:
        """
        Get Scopes.
        
        Returns:
            Dict containing scopes information
        """
        return self.client.get("scopes")
    
    def get_scope_by_id(self, scope_id: str) -> Dict:
        """
        Get Scope By Id.
        
        Args:
            scope_id: Scope identifier
            
        Returns:
            Dict containing scope information
        """
        return self.client.get(f"scopes/{scope_id}")
    
    def create_scope(self, data: Dict) -> Dict:
        """
        Create Scope.
        
        Args:
            data: Scope data
            
        Returns:
            Dict containing created scope information
        """
        return self.client.post("scopes", data=data)
    
    def delete_scope(self, scope_id: str) -> Dict:
        """
        Delete Scope.
        
        Args:
            scope_id: Scope identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"scopes/{scope_id}")
    
    def update_scope(self, scope_id: str, data: Dict) -> Dict:
        """
        Update Scope.
        
        Args:
            scope_id: Scope identifier
            data: Updated scope data
            
        Returns:
            Dict containing updated scope information
        """
        return self.client.put(f"scopes/{scope_id}", data=data)

"""
Dynamic Entity endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class DynamicEntityEndpoints:
    """Dynamic Entity-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_dynamic_entity(self, entity_name: str, data: Dict) -> Dict:
        """
        Create Dynamic Entity.
        
        Args:
            entity_name: Name of the dynamic entity
            data: Dynamic entity data
            
        Returns:
            Dict containing created dynamic entity information
        """
        return self.client.post(f"dynamic-entities/{entity_name}", data=data)
    
    def get_dynamic_entity_by_id(self, entity_name: str, entity_id: str) -> Dict:
        """
        Get Dynamic Entity by Id.
        
        Args:
            entity_name: Name of the dynamic entity
            entity_id: Dynamic entity identifier
            
        Returns:
            Dict containing dynamic entity information
        """
        return self.client.get(f"dynamic-entities/{entity_name}/{entity_id}")
    
    def get_dynamic_entities(self, entity_name: str) -> Dict:
        """
        Get Dynamic Entities.
        
        Args:
            entity_name: Name of the dynamic entity
            
        Returns:
            Dict containing dynamic entities information
        """
        return self.client.get(f"dynamic-entities/{entity_name}")
    
    def update_dynamic_entity(self, entity_name: str, entity_id: str, data: Dict) -> Dict:
        """
        Update Dynamic Entity.
        
        Args:
            entity_name: Name of the dynamic entity
            entity_id: Dynamic entity identifier
            data: Updated dynamic entity data
            
        Returns:
            Dict containing updated dynamic entity information
        """
        return self.client.put(f"dynamic-entities/{entity_name}/{entity_id}", data=data)
    
    def delete_dynamic_entity(self, entity_name: str, entity_id: str) -> Dict:
        """
        Delete Dynamic Entity.
        
        Args:
            entity_name: Name of the dynamic entity
            entity_id: Dynamic entity identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"dynamic-entities/{entity_name}/{entity_id}")

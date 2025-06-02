"""
Dynamic Resource Doc endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class DynamicResourceDocEndpoints:
    """Dynamic Resource Doc-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_dynamic_resource_doc(self, data: Dict) -> Dict:
        """
        Create Dynamic Resource Doc.
        
        Args:
            data: Dynamic resource doc data
            
        Returns:
            Dict containing created dynamic resource doc information
        """
        return self.client.post("management/dynamic-resource-docs", data=data)
    
    def get_dynamic_resource_doc(self, dynamic_resource_doc_id: str) -> Dict:
        """
        Get Dynamic Resource Doc.
        
        Args:
            dynamic_resource_doc_id: Dynamic resource doc identifier
            
        Returns:
            Dict containing dynamic resource doc information
        """
        return self.client.get(f"management/dynamic-resource-docs/{dynamic_resource_doc_id}")
    
    def get_dynamic_resource_docs(self) -> Dict:
        """
        Get Dynamic Resource Docs.
        
        Returns:
            Dict containing dynamic resource docs information
        """
        return self.client.get("management/dynamic-resource-docs")
    
    def update_dynamic_resource_doc(self, dynamic_resource_doc_id: str, data: Dict) -> Dict:
        """
        Update Dynamic Resource Doc.
        
        Args:
            dynamic_resource_doc_id: Dynamic resource doc identifier
            data: Updated dynamic resource doc data
            
        Returns:
            Dict containing updated dynamic resource doc information
        """
        return self.client.put(f"management/dynamic-resource-docs/{dynamic_resource_doc_id}", data=data)
    
    def delete_dynamic_resource_doc(self, dynamic_resource_doc_id: str) -> Dict:
        """
        Delete Dynamic Resource Doc.
        
        Args:
            dynamic_resource_doc_id: Dynamic resource doc identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"management/dynamic-resource-docs/{dynamic_resource_doc_id}")

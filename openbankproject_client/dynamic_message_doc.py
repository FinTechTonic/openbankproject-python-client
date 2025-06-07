"""
Dynamic Message Doc endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class DynamicMessageDocEndpoints:
    """Dynamic Message Doc-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_dynamic_message_doc(self, data: Dict) -> Dict:
        """
        Create Dynamic Message Doc.
        
        Args:
            data: Dynamic message doc data
            
        Returns:
            Dict containing created dynamic message doc information
        """
        return self.client.post("management/dynamic-message-docs", data=data)
    
    def get_dynamic_message_doc(self, dynamic_message_doc_id: str) -> Dict:
        """
        Get Dynamic Message Doc.
        
        Args:
            dynamic_message_doc_id: Dynamic message doc identifier
            
        Returns:
            Dict containing dynamic message doc information
        """
        return self.client.get(f"management/dynamic-message-docs/{dynamic_message_doc_id}")
    
    def get_dynamic_message_docs(self) -> Dict:
        """
        Get Dynamic Message Docs.
        
        Returns:
            Dict containing dynamic message docs information
        """
        return self.client.get("management/dynamic-message-docs")
    
    def update_dynamic_message_doc(self, dynamic_message_doc_id: str, data: Dict) -> Dict:
        """
        Update Dynamic Message Doc.
        
        Args:
            dynamic_message_doc_id: Dynamic message doc identifier
            data: Updated dynamic message doc data
            
        Returns:
            Dict containing updated dynamic message doc information
        """
        return self.client.put(f"management/dynamic-message-docs/{dynamic_message_doc_id}", data=data)
    
    def delete_dynamic_message_doc(self, dynamic_message_doc_id: str) -> Dict:
        """
        Delete Dynamic Message Doc.
        
        Args:
            dynamic_message_doc_id: Dynamic message doc identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"management/dynamic-message-docs/{dynamic_message_doc_id}")

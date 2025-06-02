"""
Account Metadata endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class AccountMetadataEndpoints:
    """Account Metadata-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_tag_on_account(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Create a tag on account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Tag data
            
        Returns:
            Dict containing created tag information
        """
        return self.client.post(f"banks/{bank_id}/accounts/{account_id}/{view_id}/metadata/tags", data=data)
    
    def get_tags_on_account(self, bank_id: str, account_id: str, view_id: str) -> Dict:
        """
        Get tags on account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            
        Returns:
            Dict containing tags information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/{view_id}/metadata/tags")
    
    def delete_tag_on_account(self, bank_id: str, account_id: str, view_id: str, tag_id: str) -> Dict:
        """
        Delete a tag on account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            tag_id: Tag identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/accounts/{account_id}/{view_id}/metadata/tags/{tag_id}")

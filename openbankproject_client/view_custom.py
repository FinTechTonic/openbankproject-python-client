"""
View Custom endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class ViewCustomEndpoints:
    """View Custom-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_custom_view(self, bank_id: str, account_id: str, data: Dict) -> Dict:
        """
        Create Custom View.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            data: Custom view data
            
        Returns:
            Dict containing created custom view information
        """
        return self.client.post(f"banks/{bank_id}/accounts/{account_id}/views", data=data)
    
    def get_custom_view(self, bank_id: str, account_id: str, view_id: str) -> Dict:
        """
        Get Custom View.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            
        Returns:
            Dict containing custom view information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/views/{view_id}")
    
    def get_views_for_account(self, bank_id: str, account_id: str) -> Dict:
        """
        Get Views for Account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            
        Returns:
            Dict containing views information for the account
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/views")
    
    def update_custom_view(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Update Custom View.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Updated custom view data
            
        Returns:
            Dict containing updated custom view information
        """
        return self.client.put(f"banks/{bank_id}/accounts/{account_id}/views/{view_id}", data=data)
    
    def delete_custom_view(self, bank_id: str, account_id: str, view_id: str) -> Dict:
        """
        Delete Custom View.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/accounts/{account_id}/views/{view_id}")
    
    def get_account_access_for_user(self, bank_id: str, account_id: str, user_id: str) -> Dict:
        """
        Get Account access for User.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            user_id: User identifier
            
        Returns:
            Dict containing account access information for the user
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/permissions/{user_id}/views")
    
    def get_access(self, bank_id: str, account_id: str) -> Dict:
        """
        Get access.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            
        Returns:
            Dict containing access information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/permissions")

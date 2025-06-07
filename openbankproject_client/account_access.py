"""
Account Access endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class AccountAccessEndpoints:
    """Account Access-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def get_account_access(self, bank_id: str, account_id: str, view_id: str) -> Dict:
        """
        Get Account Access.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            
        Returns:
            Dict containing account access information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/permissions/{view_id}/views")
    
    def grant_user_access_to_view(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Grant User Access to View.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: User access data
            
        Returns:
            Dict containing granted access information
        """
        return self.client.post(f"banks/{bank_id}/accounts/{account_id}/permissions/{view_id}/views", data=data)
    
    def revoke_user_access_to_view(self, bank_id: str, account_id: str, view_id: str, user_id: str) -> Dict:
        """
        Revoke User Access to View.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            user_id: User identifier
            
        Returns:
            Dict containing revocation status
        """
        return self.client.delete(f"banks/{bank_id}/accounts/{account_id}/permissions/{view_id}/views/{user_id}")
    
    def get_users_with_access_to_view(self, bank_id: str, account_id: str, view_id: str) -> Dict:
        """
        Get Users with Access to View.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            
        Returns:
            Dict containing users with access information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/permissions/{view_id}/views/users")

"""
Account Holder endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class AccountHolderEndpoints:
    """Account Holder-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def get_account_holders_at_bank(self, bank_id: str) -> Dict:
        """
        Get Account Holders at Bank.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing account holders information
        """
        return self.client.get(f"banks/{bank_id}/account-holders")
    
    def get_account_holders_by_account_id(self, bank_id: str, account_id: str) -> Dict:
        """
        Get Account Holders by Account Id.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            
        Returns:
            Dict containing account holders information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/account-holders")
    
    def create_account_holder(self, bank_id: str, account_id: str, data: Dict) -> Dict:
        """
        Create Account Holder.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            data: Account holder data
            
        Returns:
            Dict containing created account holder information
        """
        return self.client.post(f"banks/{bank_id}/accounts/{account_id}/account-holders", data=data)
    
    def delete_account_holder(self, bank_id: str, account_id: str, user_id: str) -> Dict:
        """
        Delete Account Holder.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            user_id: User identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/accounts/{account_id}/account-holders/{user_id}")

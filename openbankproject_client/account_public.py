"""
Account Public endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class AccountPublicEndpoints:
    """Account Public-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def get_public_account_by_id(self, bank_id: str, account_id: str) -> Dict:
        """
        Get Public Account by Id.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            
        Returns:
            Dict containing public account information
        """
        return self.client.get(f"banks/{bank_id}/public/accounts/{account_id}")
    
    def get_public_accounts_at_bank(self, bank_id: str) -> Dict:
        """
        Get Public Accounts at Bank.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing public accounts information at the specified bank
        """
        return self.client.get(f"banks/{bank_id}/public/accounts")
    
    def get_public_accounts_at_all_banks(self) -> Dict:
        """
        Get Public Accounts at all Banks.
        
        Returns:
            Dict containing public accounts information at all banks
        """
        return self.client.get("public/accounts")

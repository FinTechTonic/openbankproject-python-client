"""
Counterparty endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class CounterpartyEndpoints:
    """Counterparty-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_counterparty_explicit(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Create Counterparty (Explicit).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Counterparty data
            
        Returns:
            Dict containing created counterparty information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/counterparties", 
            data=data
        )
    
    def create_counterparty_for_any_account(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Create Counterparty for any account (Explicit).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Counterparty data
            
        Returns:
            Dict containing created counterparty information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/counterparties/any", 
            data=data
        )
    
    def get_counterparties_explicit(self, bank_id: str, account_id: str, view_id: str) -> Dict:
        """
        Get Counterparties (Explicit).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            
        Returns:
            Dict containing counterparties information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/counterparties"
        )
    
    def get_counterparties_for_any_account(self, bank_id: str, account_id: str, view_id: str) -> Dict:
        """
        Get Counterparties for any account (Explicit).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            
        Returns:
            Dict containing counterparties information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/counterparties/any"
        )
    
    def get_counterparty_by_id_explicit(self, bank_id: str, account_id: str, view_id: str, counterparty_id: str) -> Dict:
        """
        Get Counterparty by Id (Explicit).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            counterparty_id: Counterparty identifier
            
        Returns:
            Dict containing counterparty information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/counterparties/{counterparty_id}"
        )
    
    def get_counterparty_by_id_for_any_account(self, bank_id: str, account_id: str, view_id: str, counterparty_id: str) -> Dict:
        """
        Get Counterparty by Id for any account (Explicit).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            counterparty_id: Counterparty identifier
            
        Returns:
            Dict containing counterparty information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/counterparties/any/{counterparty_id}"
        )
    
    def get_counterparty_by_name_for_any_account(self, bank_id: str, account_id: str, view_id: str, name: str) -> Dict:
        """
        Get Counterparty by name for any account (Explicit).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            name: Counterparty name
            
        Returns:
            Dict containing counterparty information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/counterparties/any/name/{name}"
        )
    
    def get_other_account_by_id(self, bank_id: str, account_id: str, view_id: str, other_account_id: str) -> Dict:
        """
        Get Other Account by Id.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            
        Returns:
            Dict containing other account information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}"
        )
    
    def get_other_accounts_of_one_account(self, bank_id: str, account_id: str, view_id: str) -> Dict:
        """
        Get Other Accounts of one Account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            
        Returns:
            Dict containing other accounts information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts"
        )
    
    def delete_counterparty_explicit(self, bank_id: str, account_id: str, view_id: str, counterparty_id: str) -> Dict:
        """
        Delete Counterparty (Explicit).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            counterparty_id: Counterparty identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/counterparties/{counterparty_id}"
        )
    
    def delete_counterparty_for_any_account(self, bank_id: str, account_id: str, view_id: str, counterparty_id: str) -> Dict:
        """
        Delete Counterparty for any account (Explicit).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            counterparty_id: Counterparty identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/counterparties/any/{counterparty_id}"
        )

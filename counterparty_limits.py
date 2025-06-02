"""
Counterparty Limits endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class CounterpartyLimitsEndpoints:
    """Counterparty Limits-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_counterparty_limit(self, bank_id: str, account_id: str, view_id: str, counterparty_id: str, data: Dict) -> Dict:
        """
        Create Counterparty Limit.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            counterparty_id: Counterparty identifier
            data: Counterparty limit data
            
        Returns:
            Dict containing created counterparty limit information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/counterparties/{counterparty_id}/limits", 
            data=data
        )
    
    def get_counterparty_limit(self, bank_id: str, account_id: str, view_id: str, counterparty_id: str) -> Dict:
        """
        Get Counterparty Limit.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            counterparty_id: Counterparty identifier
            
        Returns:
            Dict containing counterparty limit information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/counterparties/{counterparty_id}/limits"
        )
    
    def get_counterparty_limit_status(self, bank_id: str, account_id: str, view_id: str, counterparty_id: str) -> Dict:
        """
        Get Counterparty Limit Status.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            counterparty_id: Counterparty identifier
            
        Returns:
            Dict containing counterparty limit status
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/counterparties/{counterparty_id}/limits/status"
        )
    
    def update_counterparty_limit(self, bank_id: str, account_id: str, view_id: str, counterparty_id: str, data: Dict) -> Dict:
        """
        Update Counterparty Limit.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            counterparty_id: Counterparty identifier
            data: Updated counterparty limit data
            
        Returns:
            Dict containing updated counterparty limit information
        """
        return self.client.put(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/counterparties/{counterparty_id}/limits", 
            data=data
        )
    
    def delete_counterparty_limit(self, bank_id: str, account_id: str, view_id: str, counterparty_id: str) -> Dict:
        """
        Delete Counterparty Limit.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            counterparty_id: Counterparty identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/counterparties/{counterparty_id}/limits"
        )

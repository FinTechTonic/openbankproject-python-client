"""
Direct Debit endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class DirectDebitEndpoints:
    """Direct Debit-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_direct_debit(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Create Direct Debit.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Direct debit data
            
        Returns:
            Dict containing created direct debit information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/direct-debit", 
            data=data
        )
    
    def create_direct_debit_management(self, bank_id: str, account_id: str, data: Dict) -> Dict:
        """
        Create Direct Debit (management).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            data: Direct debit management data
            
        Returns:
            Dict containing created direct debit information
        """
        return self.client.post(
            f"management/banks/{bank_id}/accounts/{account_id}/direct-debit", 
            data=data
        )

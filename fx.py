"""
FX endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class FxEndpoints:
    """FX-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_fx(self, bank_id: str, data: Dict) -> Dict:
        """
        Create Fx.
        
        Args:
            bank_id: Bank identifier
            data: FX data
            
        Returns:
            Dict containing created FX information
        """
        return self.client.post(f"banks/{bank_id}/fx", data=data)
    
    def get_currencies_at_bank(self, bank_id: str) -> Dict:
        """
        Get Currencies at a Bank.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing currencies information
        """
        return self.client.get(f"banks/{bank_id}/currencies")
    
    def get_current_fx_rate(self, bank_id: str, from_currency: str, to_currency: str) -> Dict:
        """
        Get Current FxRate.
        
        Args:
            bank_id: Bank identifier
            from_currency: Source currency code
            to_currency: Target currency code
            
        Returns:
            Dict containing FX rate information
        """
        return self.client.get(f"banks/{bank_id}/fx/{from_currency}/{to_currency}")

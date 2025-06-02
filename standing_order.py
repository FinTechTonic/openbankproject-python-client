"""
Standing Order endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class StandingOrderEndpoints:
    """Standing Order-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_standing_order(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Create Standing Order.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Standing order data
            
        Returns:
            Dict containing created standing order information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/standing-order", 
            data=data
        )
    
    def create_standing_order_management(self, bank_id: str, account_id: str, data: Dict) -> Dict:
        """
        Create Standing Order (management).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            data: Standing order management data
            
        Returns:
            Dict containing created standing order information
        """
        return self.client.post(
            f"management/banks/{bank_id}/accounts/{account_id}/standing-order", 
            data=data
        )

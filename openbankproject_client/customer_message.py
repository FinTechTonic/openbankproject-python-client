"""
Customer Message endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class CustomerMessageEndpoints:
    """Customer Message-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_customer_message(self, bank_id: str, customer_id: str, data: Dict) -> Dict:
        """
        Create Customer Message.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            data: Message data
            
        Returns:
            Dict containing created message information
        """
        return self.client.post(f"banks/{bank_id}/customers/{customer_id}/messages", data=data)
    
    def get_customer_messages_for_customer(self, bank_id: str, customer_id: str) -> Dict:
        """
        Get Customer Messages for a Customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing customer messages information
        """
        return self.client.get(f"banks/{bank_id}/customers/{customer_id}/messages")
    
    def get_customer_messages_for_all_customers(self, bank_id: str) -> Dict:
        """
        Get Customer Messages for all Customers.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing customer messages information for all customers
        """
        return self.client.get(f"banks/{bank_id}/customers/messages")

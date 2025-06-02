"""
Extended Bank endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class ExtendedBankEndpoints:
    """Extended Bank-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def get_bank_accounts(self, bank_id: str) -> Dict:
        """
        Get accounts at a specific bank (Authenticated access).
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing account information
        """
        return self.client.get(f"banks/{bank_id}/accounts")
    
    def get_bank_account(self, bank_id: str, account_id: str) -> Dict:
        """
        Get account by ID at a specific bank.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            
        Returns:
            Dict containing account information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}")
    
    def get_bank_account_balances(self, bank_id: str, account_id: str) -> Dict:
        """
        Get account balances.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            
        Returns:
            Dict containing account balance information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/balances")
    
    def get_bank_account_transactions(
        self, 
        bank_id: str, 
        account_id: str,
        params: Optional[Dict] = None
    ) -> Dict:
        """
        Get transactions for an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            params: Optional query parameters like from_date, to_date, limit, offset, etc.
            
        Returns:
            Dict containing transaction information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/transactions", params=params)
    
    def get_transaction(self, bank_id: str, account_id: str, transaction_id: str) -> Dict:
        """
        Get transaction by ID.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            transaction_id: Transaction identifier
            
        Returns:
            Dict containing transaction information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/transactions/{transaction_id}")
    
    def create_transaction_request(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Create a transaction request.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Transaction request data
            
        Returns:
            Dict containing transaction request information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/SANDBOX/transaction-requests",
            data=data
        )
    
    def get_bank_customers(self, bank_id: str) -> Dict:
        """
        Get customers at a specific bank.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing customer information
        """
        return self.client.get(f"banks/{bank_id}/customers")
    
    def get_customer(self, bank_id: str, customer_id: str) -> Dict:
        """
        Get customer by ID.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing customer information
        """
        return self.client.get(f"banks/{bank_id}/customers/{customer_id}")
    
    def create_customer(self, bank_id: str, data: Dict) -> Dict:
        """
        Create a customer.
        
        Args:
            bank_id: Bank identifier
            data: Customer data
            
        Returns:
            Dict containing created customer information
        """
        return self.client.post(f"banks/{bank_id}/customers", data=data)
    
    def update_customer(self, bank_id: str, customer_id: str, data: Dict) -> Dict:
        """
        Update a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            data: Updated customer data
            
        Returns:
            Dict containing updated customer information
        """
        return self.client.put(f"banks/{bank_id}/customers/{customer_id}", data=data)
    
    def get_bank_branches(self, bank_id: str) -> Dict:
        """
        Get branches for a bank.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing branch information
        """
        return self.client.get(f"banks/{bank_id}/branches")
    
    def get_bank_atms(self, bank_id: str) -> Dict:
        """
        Get ATMs for a bank.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing ATM information
        """
        return self.client.get(f"banks/{bank_id}/atms")
    
    def get_bank_products(self, bank_id: str) -> Dict:
        """
        Get products for a bank.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing product information
        """
        return self.client.get(f"banks/{bank_id}/products")
    
    def get_bank_product(self, bank_id: str, product_id: str) -> Dict:
        """
        Get product by ID.
        
        Args:
            bank_id: Bank identifier
            product_id: Product identifier
            
        Returns:
            Dict containing product information
        """
        return self.client.get(f"banks/{bank_id}/products/{product_id}")
    
    def get_bank_attributes(self, bank_id: str) -> Dict:
        """
        Get attributes for a bank.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing bank attribute information
        """
        return self.client.get(f"banks/{bank_id}/attributes")
    
    def add_bank_attribute(self, bank_id: str, data: Dict) -> Dict:
        """
        Add an attribute to a bank.
        
        Args:
            bank_id: Bank identifier
            data: Attribute data
            
        Returns:
            Dict containing added attribute information
        """
        return self.client.post(f"banks/{bank_id}/attributes", data=data)
    
    def update_bank_attribute(self, bank_id: str, attribute_id: str, data: Dict) -> Dict:
        """
        Update an attribute of a bank.
        
        Args:
            bank_id: Bank identifier
            attribute_id: Attribute identifier
            data: Updated attribute data
            
        Returns:
            Dict containing updated attribute information
        """
        return self.client.put(f"banks/{bank_id}/attributes/{attribute_id}", data=data)
    
    def delete_bank_attribute(self, bank_id: str, attribute_id: str) -> Dict:
        """
        Delete an attribute from a bank.
        
        Args:
            bank_id: Bank identifier
            attribute_id: Attribute identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/attributes/{attribute_id}")
    
    def delete_bank_customer(self, bank_id: str, customer_id: str) -> Dict:
        """
        Delete a customer at a specific bank.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/customers/{customer_id}")

"""
Customer endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class CustomerEndpoints:
    """Customer-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def get_customers(self, bank_id: str, params: Optional[Dict] = None) -> Dict:
        """
        Get all customers at a specific bank.
        
        Args:
            bank_id: Bank identifier
            params: Optional query parameters like limit, offset, etc.
            
        Returns:
            Dict containing customer information
        """
        return self.client.get(f"banks/{bank_id}/customers", params=params)
    
    def get_customer_by_id(self, bank_id: str, customer_id: str) -> Dict:
        """
        Get customer by ID at a specific bank.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing customer information
        """
        return self.client.get(f"banks/{bank_id}/customers/{customer_id}")
    
    def create_customer(self, bank_id: str, data: Dict) -> Dict:
        """
        Create a new customer at a specific bank.
        
        Args:
            bank_id: Bank identifier
            data: Customer data
            
        Returns:
            Dict containing created customer information
        """
        return self.client.post(f"banks/{bank_id}/customers", data=data)
    
    def update_customer(self, bank_id: str, customer_id: str, data: Dict) -> Dict:
        """
        Update an existing customer at a specific bank.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            data: Updated customer data
            
        Returns:
            Dict containing updated customer information
        """
        return self.client.put(f"banks/{bank_id}/customers/{customer_id}", data=data)
    
    def delete_customer(self, bank_id: str, customer_id: str) -> Dict:
        """
        Delete a customer at a specific bank.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/customers/{customer_id}")
    
    def get_customer_attributes(self, bank_id: str, customer_id: str) -> Dict:
        """
        Get attributes for a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing customer attribute information
        """
        return self.client.get(f"banks/{bank_id}/customers/{customer_id}/attributes")
    
    def add_customer_attribute(self, bank_id: str, customer_id: str, data: Dict) -> Dict:
        """
        Add an attribute to a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            data: Attribute data
            
        Returns:
            Dict containing added attribute information
        """
        return self.client.post(f"banks/{bank_id}/customers/{customer_id}/attributes", data=data)
    
    def update_customer_attribute(self, bank_id: str, customer_id: str, attribute_id: str, data: Dict) -> Dict:
        """
        Update an attribute of a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            attribute_id: Attribute identifier
            data: Updated attribute data
            
        Returns:
            Dict containing updated attribute information
        """
        return self.client.put(f"banks/{bank_id}/customers/{customer_id}/attributes/{attribute_id}", data=data)
    
    def delete_customer_attribute(self, bank_id: str, customer_id: str, attribute_id: str) -> Dict:
        """
        Delete an attribute from a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            attribute_id: Attribute identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/customers/{customer_id}/attributes/{attribute_id}")
    
    def get_customer_messages(self, bank_id: str, customer_id: str) -> Dict:
        """
        Get messages for a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing customer message information
        """
        return self.client.get(f"banks/{bank_id}/customers/{customer_id}/messages")
    
    def add_customer_message(self, bank_id: str, customer_id: str, data: Dict) -> Dict:
        """
        Add a message to a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            data: Message data
            
        Returns:
            Dict containing added message information
        """
        return self.client.post(f"banks/{bank_id}/customers/{customer_id}/messages", data=data)
    
    def update_customer_message(self, bank_id: str, customer_id: str, message_id: str, data: Dict) -> Dict:
        """
        Update a message of a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            message_id: Message identifier
            data: Updated message data
            
        Returns:
            Dict containing updated message information
        """
        return self.client.put(f"banks/{bank_id}/customers/{customer_id}/messages/{message_id}", data=data)
    
    def delete_customer_message(self, bank_id: str, customer_id: str, message_id: str) -> Dict:
        """
        Delete a message from a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            message_id: Message identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/customers/{customer_id}/messages/{message_id}")
    
    def get_customer_kyc_status(self, bank_id: str, customer_id: str) -> Dict:
        """
        Get KYC status for a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing customer KYC status information
        """
        return self.client.get(f"banks/{bank_id}/customers/{customer_id}/kyc/status")
    
    def get_customer_kyc_media(self, bank_id: str, customer_id: str) -> Dict:
        """
        Get KYC media for a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing customer KYC media information
        """
        return self.client.get(f"banks/{bank_id}/customers/{customer_id}/kyc/media")
    
    def get_customer_kyc_documents(self, bank_id: str, customer_id: str) -> Dict:
        """
        Get KYC documents for a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing customer KYC document information
        """
        return self.client.get(f"banks/{bank_id}/customers/{customer_id}/kyc/documents")
    
    def get_customer_kyc_checks(self, bank_id: str, customer_id: str) -> Dict:
        """
        Get KYC checks for a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing customer KYC check information
        """
        return self.client.get(f"banks/{bank_id}/customers/{customer_id}/kyc/checks")
    
    def get_customer_user_links(self, bank_id: str, customer_id: str) -> Dict:
        """
        Get user links for a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing customer user link information
        """
        return self.client.get(f"banks/{bank_id}/customers/{customer_id}/user-links")
    
    def create_customer_user_link(self, bank_id: str, customer_id: str, data: Dict) -> Dict:
        """
        Create a user link for a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            data: User link data
            
        Returns:
            Dict containing created user link information
        """
        return self.client.post(f"banks/{bank_id}/customers/{customer_id}/user-links", data=data)
    
    def update_customer_user_link(self, bank_id: str, customer_id: str, link_id: str, data: Dict) -> Dict:
        """
        Update a user link for a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            link_id: User link identifier
            data: Updated user link data
            
        Returns:
            Dict containing updated user link information
        """
        return self.client.put(f"banks/{bank_id}/customers/{customer_id}/user-links/{link_id}", data=data)
    
    def delete_customer_user_link(self, bank_id: str, customer_id: str, link_id: str) -> Dict:
        """
        Delete a user link from a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            link_id: User link identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/customers/{customer_id}/user-links/{link_id}")
    
    def get_customer_account_links(self, bank_id: str, customer_id: str) -> Dict:
        """
        Get account links for a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing customer account link information
        """
        return self.client.get(f"banks/{bank_id}/customers/{customer_id}/account-links")
    
    def create_customer_account_link(self, bank_id: str, customer_id: str, data: Dict) -> Dict:
        """
        Create an account link for a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            data: Account link data
            
        Returns:
            Dict containing created account link information
        """
        return self.client.post(f"banks/{bank_id}/customers/{customer_id}/account-links", data=data)
    
    def update_customer_account_link(self, bank_id: str, customer_id: str, link_id: str, data: Dict) -> Dict:
        """
        Update an account link for a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            link_id: Account link identifier
            data: Updated account link data
            
        Returns:
            Dict containing updated account link information
        """
        return self.client.put(f"banks/{bank_id}/customers/{customer_id}/account-links/{link_id}", data=data)
    
    def delete_customer_account_link(self, bank_id: str, customer_id: str, link_id: str) -> Dict:
        """
        Delete an account link from a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            link_id: Account link identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/customers/{customer_id}/account-links/{link_id}")

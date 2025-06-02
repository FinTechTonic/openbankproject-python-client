"""
KYC endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class KycEndpoints:
    """KYC-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def add_kyc_check(self, bank_id: str, customer_id: str, data: Dict) -> Dict:
        """
        Add KYC Check.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            data: KYC check data
            
        Returns:
            Dict containing created KYC check information
        """
        return self.client.post(f"banks/{bank_id}/customers/{customer_id}/kyc_check", data=data)
    
    def add_kyc_document(self, bank_id: str, customer_id: str, data: Dict) -> Dict:
        """
        Add KYC Document.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            data: KYC document data
            
        Returns:
            Dict containing created KYC document information
        """
        return self.client.post(f"banks/{bank_id}/customers/{customer_id}/kyc_documents", data=data)
    
    def add_kyc_media(self, bank_id: str, customer_id: str, data: Dict) -> Dict:
        """
        Add KYC Media.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            data: KYC media data
            
        Returns:
            Dict containing created KYC media information
        """
        return self.client.post(f"banks/{bank_id}/customers/{customer_id}/kyc_media", data=data)
    
    def add_kyc_status(self, bank_id: str, customer_id: str, data: Dict) -> Dict:
        """
        Add KYC Status.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            data: KYC status data
            
        Returns:
            Dict containing created KYC status information
        """
        return self.client.post(f"banks/{bank_id}/customers/{customer_id}/kyc_statuses", data=data)
    
    def get_customer_kyc_checks(self, bank_id: str, customer_id: str) -> Dict:
        """
        Get Customer KYC Checks.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing KYC checks information
        """
        return self.client.get(f"banks/{bank_id}/customers/{customer_id}/kyc_checks")
    
    def get_customer_kyc_documents(self, bank_id: str, customer_id: str) -> Dict:
        """
        Get Customer KYC Documents.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing KYC documents information
        """
        return self.client.get(f"banks/{bank_id}/customers/{customer_id}/kyc_documents")
    
    def get_customer_kyc_statuses(self, bank_id: str, customer_id: str) -> Dict:
        """
        Get Customer KYC statuses.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing KYC statuses information
        """
        return self.client.get(f"banks/{bank_id}/customers/{customer_id}/kyc_statuses")
    
    def get_kyc_media_for_customer(self, bank_id: str, customer_id: str) -> Dict:
        """
        Get KYC Media for a customer.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing KYC media information
        """
        return self.client.get(f"banks/{bank_id}/customers/{customer_id}/kyc_media")

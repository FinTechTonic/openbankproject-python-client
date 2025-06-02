"""
Account Application endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class AccountApplicationEndpoints:
    """Account Application-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_account_application(self, bank_id: str, data: Dict) -> Dict:
        """
        Create Account Application.
        
        Args:
            bank_id: Bank identifier
            data: Account application data
            
        Returns:
            Dict containing created account application information
        """
        return self.client.post(f"banks/{bank_id}/account-applications", data=data)
    
    def get_account_application_by_id(self, bank_id: str, account_application_id: str) -> Dict:
        """
        Get Account Application by Id.
        
        Args:
            bank_id: Bank identifier
            account_application_id: Account application identifier
            
        Returns:
            Dict containing account application information
        """
        return self.client.get(f"banks/{bank_id}/account-applications/{account_application_id}")
    
    def get_account_applications(self, bank_id: str) -> Dict:
        """
        Get Account Applications.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing account applications information
        """
        return self.client.get(f"banks/{bank_id}/account-applications")
    
    def update_account_application_status(self, bank_id: str, account_application_id: str, data: Dict) -> Dict:
        """
        Update Account Application Status.
        
        Args:
            bank_id: Bank identifier
            account_application_id: Account application identifier
            data: Updated status data
            
        Returns:
            Dict containing updated account application information
        """
        return self.client.put(f"banks/{bank_id}/account-applications/{account_application_id}", data=data)

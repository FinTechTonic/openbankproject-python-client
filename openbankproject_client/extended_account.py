"""
Extended Account endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class ExtendedAccountEndpoints:
    """Extended Account-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def get_account_by_id(self, account_id: str) -> Dict:
        """
        Get account by ID (across all banks).
        
        Args:
            account_id: Account identifier
            
        Returns:
            Dict containing account information
        """
        return self.client.get(f"accounts/{account_id}")
    
    def get_account_views(self, bank_id: str, account_id: str) -> Dict:
        """
        Get views for an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            
        Returns:
            Dict containing view information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/views")
    
    def create_account_view(self, bank_id: str, account_id: str, data: Dict) -> Dict:
        """
        Create a view for an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            data: View data
            
        Returns:
            Dict containing created view information
        """
        return self.client.post(f"banks/{bank_id}/accounts/{account_id}/views", data=data)
    
    def update_account_view(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Update a view for an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Updated view data
            
        Returns:
            Dict containing updated view information
        """
        return self.client.put(f"banks/{bank_id}/accounts/{account_id}/views/{view_id}", data=data)
    
    def delete_account_view(self, bank_id: str, account_id: str, view_id: str) -> Dict:
        """
        Delete a view for an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/accounts/{account_id}/views/{view_id}")
    
    def get_account_permissions(self, bank_id: str, account_id: str) -> Dict:
        """
        Get permissions for an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            
        Returns:
            Dict containing permission information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/permissions")
    
    def grant_account_access(self, bank_id: str, account_id: str, data: Dict) -> Dict:
        """
        Grant access to an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            data: Access grant data
            
        Returns:
            Dict containing grant status
        """
        return self.client.post(f"banks/{bank_id}/accounts/{account_id}/permissions", data=data)
    
    def revoke_account_access(self, bank_id: str, account_id: str, provider: str, user_id: str) -> Dict:
        """
        Revoke access to an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            provider: Provider identifier
            user_id: User identifier
            
        Returns:
            Dict containing revocation status
        """
        return self.client.delete(f"banks/{bank_id}/accounts/{account_id}/permissions/{provider}/{user_id}")
    
    def create_account(self, bank_id: str, data: Dict) -> Dict:
        """
        Create a new account.
        
        Args:
            bank_id: Bank identifier
            data: Account data
            
        Returns:
            Dict containing created account information
        """
        return self.client.post(f"banks/{bank_id}/accounts", data=data)
    
    def close_account(self, bank_id: str, account_id: str) -> Dict:
        """
        Close an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            
        Returns:
            Dict containing closure status
        """
        return self.client.delete(f"banks/{bank_id}/accounts/{account_id}")
        
    def check_available_funds(self, bank_id: str, account_id: str, view_id: str, amount: str, currency: str) -> Dict:
        """
        Check if an account has available funds.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            amount: Amount to check
            currency: Currency of the amount
            
        Returns:
            Dict containing available funds information
        """
        params = {
            "amount": amount,
            "currency": currency
        }
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/{view_id}/funds-available", params=params)
    
    def get_account_with_balance(self, bank_id: str, account_id: str) -> Dict:
        """
        Get account by ID with balance.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            
        Returns:
            Dict containing account information with balance
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/balance")
    
    def update_account_label(self, bank_id: str, account_id: str, data: Dict) -> Dict:
        """
        Update account label.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            data: Updated label data
            
        Returns:
            Dict containing updated account information
        """
        return self.client.put(f"banks/{bank_id}/accounts/{account_id}/label", data=data)
    
    def get_account_attributes(self, bank_id: str, account_id: str) -> Dict:
        """
        Get attributes for an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            
        Returns:
            Dict containing account attribute information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/attributes")
    
    def add_account_attribute(self, bank_id: str, account_id: str, data: Dict) -> Dict:
        """
        Add an attribute to an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            data: Attribute data
            
        Returns:
            Dict containing added attribute information
        """
        return self.client.post(f"banks/{bank_id}/accounts/{account_id}/attributes", data=data)
    
    def update_account_attribute(self, bank_id: str, account_id: str, attribute_id: str, data: Dict) -> Dict:
        """
        Update an attribute of an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            attribute_id: Attribute identifier
            data: Updated attribute data
            
        Returns:
            Dict containing updated attribute information
        """
        return self.client.put(f"banks/{bank_id}/accounts/{account_id}/attributes/{attribute_id}", data=data)
    
    def delete_account_attribute(self, bank_id: str, account_id: str, attribute_id: str) -> Dict:
        """
        Delete an attribute from an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            attribute_id: Attribute identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/accounts/{account_id}/attributes/{attribute_id}")
    
    def get_account_tags(self, bank_id: str, account_id: str, view_id: str) -> Dict:
        """
        Get tags for an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            
        Returns:
            Dict containing account tag information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/{view_id}/tags")
    
    def add_account_tag(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Add a tag to an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Tag data
            
        Returns:
            Dict containing added tag information
        """
        return self.client.post(f"banks/{bank_id}/accounts/{account_id}/{view_id}/tags", data=data)
    
    def delete_account_tag(self, bank_id: str, account_id: str, view_id: str, tag_id: str) -> Dict:
        """
        Delete a tag from an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            tag_id: Tag identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/accounts/{account_id}/{view_id}/tags/{tag_id}")
    
    def get_account_metadata(self, bank_id: str, account_id: str, view_id: str) -> Dict:
        """
        Get metadata for an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            
        Returns:
            Dict containing account metadata information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/{view_id}/metadata")
    
    def get_account_by_iban(self, iban: str) -> Dict:
        """
        Get account by IBAN.
        
        Args:
            iban: IBAN identifier
            
        Returns:
            Dict containing account information
        """
        return self.client.get(f"accounts/iban/{iban}")
    
    def get_firehose_accounts(self, bank_id: str) -> Dict:
        """
        Get firehose accounts at a specific bank.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing firehose account information
        """
        return self.client.get(f"banks/{bank_id}/firehose/accounts")
    
    def get_firehose_transactions(self, bank_id: str, account_id: str) -> Dict:
        """
        Get firehose transactions for an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            
        Returns:
            Dict containing firehose transaction information
        """
        return self.client.get(f"banks/{bank_id}/firehose/accounts/{account_id}/transactions")
    
    def get_firehose_bank_transactions(self, bank_id: str) -> Dict:
        """
        Get firehose transactions for a bank.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing firehose bank transaction information
        """
        return self.client.get(f"banks/{bank_id}/firehose/transactions")
    
    def get_account_statistics(self, bank_id: str, account_id: str, view_id: str) -> Dict:
        """
        Get statistics for an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            
        Returns:
            Dict containing account statistics information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/{view_id}/statistics")
    
    def get_account_statements(self, bank_id: str, account_id: str) -> Dict:
        """
        Get statements for an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            
        Returns:
            Dict containing account statement information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/statements")
    
    def get_account_statement(self, bank_id: str, account_id: str, statement_id: str) -> Dict:
        """
        Get statement by ID for an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            statement_id: Statement identifier
            
        Returns:
            Dict containing account statement information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/statements/{statement_id}")
    
    def get_account_statement_transactions(self, bank_id: str, account_id: str, statement_id: str) -> Dict:
        """
        Get transactions for a statement.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            statement_id: Statement identifier
            
        Returns:
            Dict containing statement transaction information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/statements/{statement_id}/transactions")
    
    def generate_account_statement_pdf(self, bank_id: str, account_id: str, statement_id: str) -> Dict:
        """
        Generate PDF for a statement.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            statement_id: Statement identifier
            
        Returns:
            Dict containing PDF generation information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/statements/{statement_id}/pdf")

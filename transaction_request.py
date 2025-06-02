"""
Transaction Request endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class TransactionRequestEndpoints:
    """Transaction Request-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_transaction_request_account(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Create Transaction Request (ACCOUNT).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Transaction request data
            
        Returns:
            Dict containing created transaction request information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/ACCOUNT/transaction-requests", 
            data=data
        )
    
    def create_transaction_request_account_otp(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Create Transaction Request (ACCOUNT_OTP).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Transaction request data with OTP
            
        Returns:
            Dict containing created transaction request information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/ACCOUNT_OTP/transaction-requests", 
            data=data
        )
    
    def create_transaction_request_agent_cash_withdrawal(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Create Transaction Request (AGENT_CASH_WITHDRAWAL).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Transaction request data for agent cash withdrawal
            
        Returns:
            Dict containing created transaction request information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/AGENT_CASH_WITHDRAWAL/transaction-requests", 
            data=data
        )
    
    def create_transaction_request_card(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Create Transaction Request (CARD).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Transaction request data for card
            
        Returns:
            Dict containing created transaction request information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/CARD/transaction-requests", 
            data=data
        )
    
    def create_transaction_request_counterparty(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Create Transaction Request (COUNTERPARTY).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Transaction request data for counterparty
            
        Returns:
            Dict containing created transaction request information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/COUNTERPARTY/transaction-requests", 
            data=data
        )
    
    def create_transaction_request_free_form(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Create Transaction Request (FREE_FORM).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Transaction request data in free form
            
        Returns:
            Dict containing created transaction request information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/FREE_FORM/transaction-requests", 
            data=data
        )
    
    def create_transaction_request_refund(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Create Transaction Request (REFUND).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Transaction request data for refund
            
        Returns:
            Dict containing created transaction request information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/REFUND/transaction-requests", 
            data=data
        )
    
    def create_transaction_request_sandbox_tan(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Create Transaction Request (SANDBOX_TAN).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Transaction request data for sandbox TAN
            
        Returns:
            Dict containing created transaction request information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/SANDBOX_TAN/transaction-requests", 
            data=data
        )
    
    def create_transaction_request_sepa(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Create Transaction Request (SEPA).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Transaction request data for SEPA
            
        Returns:
            Dict containing created transaction request information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/SEPA/transaction-requests", 
            data=data
        )
    
    def create_transaction_request_simple(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Create Transaction Request (SIMPLE).
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Transaction request data for simple transfer
            
        Returns:
            Dict containing created transaction request information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/SIMPLE/transaction-requests", 
            data=data
        )
    
    def get_transaction_request(self, bank_id: str, account_id: str, view_id: str, transaction_request_id: str) -> Dict:
        """
        Get Transaction Request.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_request_id: Transaction request identifier
            
        Returns:
            Dict containing transaction request information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-requests/{transaction_request_id}"
        )
    
    def get_transaction_request_by_id(self, transaction_request_id: str) -> Dict:
        """
        Get Transaction Request by ID.
        
        Args:
            transaction_request_id: Transaction request identifier
            
        Returns:
            Dict containing transaction request information
        """
        return self.client.get(f"transaction-requests/{transaction_request_id}")
    
    def get_transaction_requests(self, bank_id: str, account_id: str, view_id: str) -> Dict:
        """
        Get Transaction Requests.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            
        Returns:
            Dict containing transaction requests information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-requests")
    
    def get_transaction_request_types_at_bank(self, bank_id: str) -> Dict:
        """
        Get Transaction Request Types at Bank.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing transaction request types information
        """
        return self.client.get(f"banks/{bank_id}/transaction-request-types")
    
    def get_transaction_request_types_for_account(self, bank_id: str, account_id: str, view_id: str) -> Dict:
        """
        Get Transaction Request Types for Account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            
        Returns:
            Dict containing transaction request types information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types")
    
    def create_transaction_request_attribute(self, bank_id: str, account_id: str, view_id: str, 
                                            transaction_request_id: str, data: Dict) -> Dict:
        """
        Create Transaction Request Attribute.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_request_id: Transaction request identifier
            data: Attribute data
            
        Returns:
            Dict containing created attribute information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-requests/{transaction_request_id}/attribute", 
            data=data
        )
    
    def update_transaction_request_attribute(self, bank_id: str, account_id: str, view_id: str, 
                                            transaction_request_id: str, attribute_id: str, data: Dict) -> Dict:
        """
        Update Transaction Request Attribute.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_request_id: Transaction request identifier
            attribute_id: Attribute identifier
            data: Updated attribute data
            
        Returns:
            Dict containing updated attribute information
        """
        return self.client.put(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-requests/{transaction_request_id}/attributes/{attribute_id}", 
            data=data
        )
    
    def get_transaction_request_attribute_by_id(self, bank_id: str, account_id: str, view_id: str, 
                                              transaction_request_id: str, attribute_id: str) -> Dict:
        """
        Get Transaction Request Attribute By Id.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_request_id: Transaction request identifier
            attribute_id: Attribute identifier
            
        Returns:
            Dict containing attribute information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-requests/{transaction_request_id}/attributes/{attribute_id}"
        )
    
    def get_transaction_request_attributes(self, bank_id: str, account_id: str, view_id: str, 
                                         transaction_request_id: str) -> Dict:
        """
        Get Transaction Request Attributes.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_request_id: Transaction request identifier
            
        Returns:
            Dict containing attributes information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-requests/{transaction_request_id}/attributes"
        )
    
    def get_transaction_request_attribute_definition(self, bank_id: str) -> Dict:
        """
        Get Transaction Request Attribute Definition.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing attribute definition information
        """
        return self.client.get(f"banks/{bank_id}/attribute-definitions/transaction-request")
    
    def create_or_update_transaction_request_attribute_definition(self, bank_id: str, data: Dict) -> Dict:
        """
        Create or Update Transaction Request Attribute Definition.
        
        Args:
            bank_id: Bank identifier
            data: Attribute definition data
            
        Returns:
            Dict containing created or updated attribute definition information
        """
        return self.client.put(f"banks/{bank_id}/attribute-definitions/transaction-request", data=data)
    
    def delete_transaction_request_attribute_definition(self, bank_id: str, attribute_definition_id: str) -> Dict:
        """
        Delete Transaction Request Attribute Definition.
        
        Args:
            bank_id: Bank identifier
            attribute_definition_id: Attribute definition identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/attribute-definitions/transaction-request/{attribute_definition_id}")
    
    def update_transaction_request_status(self, bank_id: str, account_id: str, view_id: str, 
                                        transaction_request_id: str, data: Dict) -> Dict:
        """
        Update Transaction Request Status.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_request_id: Transaction request identifier
            data: Updated status data
            
        Returns:
            Dict containing updated transaction request information
        """
        return self.client.put(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-requests/{transaction_request_id}/status", 
            data=data
        )
    
    def answer_transaction_request_challenge(self, bank_id: str, account_id: str, view_id: str, 
                                           transaction_request_id: str, challenge_id: str, data: Dict) -> Dict:
        """
        Answer Transaction Request Challenge.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_request_id: Transaction request identifier
            challenge_id: Challenge identifier
            data: Challenge answer data
            
        Returns:
            Dict containing challenge response information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-requests/{transaction_request_id}/challenge/{challenge_id}", 
            data=data
        )
    
    def create_historical_transactions(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Create Historical Transactions.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Historical transactions data
            
        Returns:
            Dict containing created transactions information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/historical", 
            data=data
        )
    
    def save_historical_transactions(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Save Historical Transactions.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Historical transactions data
            
        Returns:
            Dict containing saved transactions information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/historical/save", 
            data=data
        )

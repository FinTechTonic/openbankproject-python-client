"""
Transaction endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class TransactionEndpoints:
    """Transaction-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def get_transactions(self, bank_id: str, account_id: str, view_id: str, params: Optional[Dict] = None) -> Dict:
        """
        Get transactions for an account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            params: Optional query parameters like from_date, to_date, limit, offset, etc.
            
        Returns:
            Dict containing transaction information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions", params=params)
    
    def get_transaction(self, bank_id: str, account_id: str, view_id: str, transaction_id: str) -> Dict:
        """
        Get transaction by ID.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            
        Returns:
            Dict containing transaction information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}")
    
    def create_transaction(self, bank_id: str, account_id: str, view_id: str, data: Dict) -> Dict:
        """
        Create a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            data: Transaction data
            
        Returns:
            Dict containing created transaction information
        """
        return self.client.post(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions", data=data)
    
    def update_transaction(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, data: Dict) -> Dict:
        """
        Update a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            data: Updated transaction data
            
        Returns:
            Dict containing updated transaction information
        """
        return self.client.put(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}", data=data)
    
    def delete_transaction(self, bank_id: str, account_id: str, view_id: str, transaction_id: str) -> Dict:
        """
        Delete a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}")
    
    def get_transaction_attributes(self, bank_id: str, account_id: str, view_id: str, transaction_id: str) -> Dict:
        """
        Get attributes for a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            
        Returns:
            Dict containing transaction attribute information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/attributes")
    
    def add_transaction_attribute(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, data: Dict) -> Dict:
        """
        Add an attribute to a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            data: Attribute data
            
        Returns:
            Dict containing added attribute information
        """
        return self.client.post(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/attributes", data=data)
    
    def update_transaction_attribute(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, attribute_id: str, data: Dict) -> Dict:
        """
        Update an attribute of a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            attribute_id: Attribute identifier
            data: Updated attribute data
            
        Returns:
            Dict containing updated attribute information
        """
        return self.client.put(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/attributes/{attribute_id}", data=data)
    
    def delete_transaction_attribute(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, attribute_id: str) -> Dict:
        """
        Delete an attribute from a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            attribute_id: Attribute identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/attributes/{attribute_id}")
    
    def get_transaction_tags(self, bank_id: str, account_id: str, view_id: str, transaction_id: str) -> Dict:
        """
        Get tags for a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            
        Returns:
            Dict containing transaction tag information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/tags")
    
    def add_transaction_tag(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, data: Dict) -> Dict:
        """
        Add a tag to a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            data: Tag data
            
        Returns:
            Dict containing added tag information
        """
        return self.client.post(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/tags", data=data)
    
    def delete_transaction_tag(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, tag_id: str) -> Dict:
        """
        Delete a tag from a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            tag_id: Tag identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/tags/{tag_id}")
    
    def get_transaction_images(self, bank_id: str, account_id: str, view_id: str, transaction_id: str) -> Dict:
        """
        Get images for a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            
        Returns:
            Dict containing transaction image information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/images")
    
    def add_transaction_image(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, data: Dict) -> Dict:
        """
        Add an image to a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            data: Image data
            
        Returns:
            Dict containing added image information
        """
        return self.client.post(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/images", data=data)
    
    def delete_transaction_image(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, image_id: str) -> Dict:
        """
        Delete an image from a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            image_id: Image identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/images/{image_id}")
    
    def get_transaction_comments(self, bank_id: str, account_id: str, view_id: str, transaction_id: str) -> Dict:
        """
        Get comments for a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            
        Returns:
            Dict containing transaction comment information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/comments")
    
    def add_transaction_comment(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, data: Dict) -> Dict:
        """
        Add a comment to a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            data: Comment data
            
        Returns:
            Dict containing added comment information
        """
        return self.client.post(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/comments", data=data)
    
    def delete_transaction_comment(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, comment_id: str) -> Dict:
        """
        Delete a comment from a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            comment_id: Comment identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/comments/{comment_id}")
    
    def get_transaction_narratives(self, bank_id: str, account_id: str, view_id: str, transaction_id: str) -> Dict:
        """
        Get narratives for a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            
        Returns:
            Dict containing transaction narrative information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/narrative")
    
    def add_transaction_narrative(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, data: Dict) -> Dict:
        """
        Add a narrative to a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            data: Narrative data
            
        Returns:
            Dict containing added narrative information
        """
        return self.client.post(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/narrative", data=data)
    
    def update_transaction_narrative(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, data: Dict) -> Dict:
        """
        Update the narrative of a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            data: Updated narrative data
            
        Returns:
            Dict containing updated narrative information
        """
        return self.client.put(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/narrative", data=data)
    
    def delete_transaction_narrative(self, bank_id: str, account_id: str, view_id: str, transaction_id: str) -> Dict:
        """
        Delete the narrative from a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/narrative")
    
    def get_transaction_types(self) -> Dict:
        """
        Get all transaction types.
        
        Returns:
            Dict containing transaction type information
        """
        return self.client.get("transaction-types")
    
    def get_transaction_status(self, bank_id: str, account_id: str, view_id: str, transaction_id: str) -> Dict:
        """
        Get the status of a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            
        Returns:
            Dict containing transaction status information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/status")
    
    def get_transaction_challenges(self, bank_id: str, account_id: str, view_id: str, transaction_id: str) -> Dict:
        """
        Get challenges for a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            
        Returns:
            Dict containing transaction challenge information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/challenges")
    
    def answer_transaction_challenge(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, challenge_id: str, data: Dict) -> Dict:
        """
        Answer a challenge for a transaction.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            challenge_id: Challenge identifier
            data: Challenge answer data
            
        Returns:
            Dict containing challenge response information
        """
        return self.client.post(f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/challenges/{challenge_id}", data=data)

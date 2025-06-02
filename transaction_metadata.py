"""
Transaction Metadata endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class TransactionMetadataEndpoints:
    """Transaction Metadata-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def add_transaction_comment(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, data: Dict) -> Dict:
        """
        Add a Transaction Comment.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            data: Comment data
            
        Returns:
            Dict containing created comment information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/metadata/comments", 
            data=data
        )
    
    def add_transaction_image(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, data: Dict) -> Dict:
        """
        Add a Transaction Image.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            data: Image data
            
        Returns:
            Dict containing created image information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/metadata/images", 
            data=data
        )
    
    def add_transaction_narrative(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, data: Dict) -> Dict:
        """
        Add a Transaction Narrative.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            data: Narrative data
            
        Returns:
            Dict containing created narrative information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/metadata/narrative", 
            data=data
        )
    
    def add_transaction_tag(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, data: Dict) -> Dict:
        """
        Add a Transaction Tag.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            data: Tag data
            
        Returns:
            Dict containing created tag information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/metadata/tags", 
            data=data
        )
    
    def add_transaction_where_tag(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, data: Dict) -> Dict:
        """
        Add a Transaction where Tag.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            data: Where tag data
            
        Returns:
            Dict containing created where tag information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/metadata/where", 
            data=data
        )
    
    def delete_transaction_comment(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, comment_id: str) -> Dict:
        """
        Delete a Transaction Comment.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            comment_id: Comment identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/metadata/comments/{comment_id}"
        )
    
    def delete_transaction_image(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, image_id: str) -> Dict:
        """
        Delete a Transaction Image.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            image_id: Image identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/metadata/images/{image_id}"
        )
    
    def delete_transaction_narrative(self, bank_id: str, account_id: str, view_id: str, transaction_id: str) -> Dict:
        """
        Delete a Transaction Narrative.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/metadata/narrative"
        )
    
    def delete_transaction_tag(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, tag_id: str) -> Dict:
        """
        Delete a Transaction Tag.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            tag_id: Tag identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/metadata/tags/{tag_id}"
        )
    
    def get_transaction_comments(self, bank_id: str, account_id: str, view_id: str, transaction_id: str) -> Dict:
        """
        Get Transaction Comments.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            
        Returns:
            Dict containing comments information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/metadata/comments"
        )
    
    def get_transaction_images(self, bank_id: str, account_id: str, view_id: str, transaction_id: str) -> Dict:
        """
        Get Transaction Images.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            
        Returns:
            Dict containing images information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/metadata/images"
        )
    
    def get_transaction_tags(self, bank_id: str, account_id: str, view_id: str, transaction_id: str) -> Dict:
        """
        Get Transaction Tags.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            
        Returns:
            Dict containing tags information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/metadata/tags"
        )
    
    def get_transaction_narrative(self, bank_id: str, account_id: str, view_id: str, transaction_id: str) -> Dict:
        """
        Get a Transaction Narrative.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            
        Returns:
            Dict containing narrative information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/metadata/narrative"
        )
    
    def get_transaction_where_tag(self, bank_id: str, account_id: str, view_id: str, transaction_id: str) -> Dict:
        """
        Get a Transaction where Tag.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            
        Returns:
            Dict containing where tag information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/metadata/where"
        )
    
    def update_transaction_narrative(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, data: Dict) -> Dict:
        """
        Update a Transaction Narrative.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            data: Updated narrative data
            
        Returns:
            Dict containing updated narrative information
        """
        return self.client.put(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/metadata/narrative", 
            data=data
        )
    
    def update_transaction_where_tag(self, bank_id: str, account_id: str, view_id: str, transaction_id: str, data: Dict) -> Dict:
        """
        Update a Transaction where Tag.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            transaction_id: Transaction identifier
            data: Updated where tag data
            
        Returns:
            Dict containing updated where tag information
        """
        return self.client.put(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/transactions/{transaction_id}/metadata/where", 
            data=data
        )

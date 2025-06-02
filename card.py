"""
Card endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class CardEndpoints:
    """Card-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_card(self, bank_id: str, data: Dict) -> Dict:
        """
        Create a new card.
        
        Args:
            bank_id: Bank identifier
            data: Card data
            
        Returns:
            Dict containing created card information
        """
        return self.client.post(f"banks/{bank_id}/cards", data=data)
    
    def get_card_by_id(self, bank_id: str, card_id: str) -> Dict:
        """
        Get card by ID.
        
        Args:
            bank_id: Bank identifier
            card_id: Card identifier
            
        Returns:
            Dict containing card information
        """
        return self.client.get(f"banks/{bank_id}/cards/{card_id}")
    
    def get_cards_for_bank(self, bank_id: str) -> Dict:
        """
        Get cards for the specified bank.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing cards information
        """
        return self.client.get(f"banks/{bank_id}/cards")
    
    def get_cards_for_current_user(self) -> Dict:
        """
        Get cards for the current user.
        
        Returns:
            Dict containing user's cards information
        """
        return self.client.get("cards")
    
    def update_card(self, bank_id: str, card_id: str, data: Dict) -> Dict:
        """
        Update an existing card.
        
        Args:
            bank_id: Bank identifier
            card_id: Card identifier
            data: Updated card data
            
        Returns:
            Dict containing updated card information
        """
        return self.client.put(f"banks/{bank_id}/cards/{card_id}", data=data)
    
    def delete_card(self, bank_id: str, card_id: str) -> Dict:
        """
        Delete a card.
        
        Args:
            bank_id: Bank identifier
            card_id: Card identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/cards/{card_id}")
    
    def create_card_attribute(self, bank_id: str, card_id: str, data: Dict) -> Dict:
        """
        Create a card attribute.
        
        Args:
            bank_id: Bank identifier
            card_id: Card identifier
            data: Attribute data
            
        Returns:
            Dict containing created attribute information
        """
        return self.client.post(f"banks/{bank_id}/cards/{card_id}/attributes", data=data)
    
    def update_card_attribute(self, bank_id: str, card_id: str, attribute_id: str, data: Dict) -> Dict:
        """
        Update a card attribute.
        
        Args:
            bank_id: Bank identifier
            card_id: Card identifier
            attribute_id: Attribute identifier
            data: Updated attribute data
            
        Returns:
            Dict containing updated attribute information
        """
        return self.client.put(f"banks/{bank_id}/cards/{card_id}/attributes/{attribute_id}", data=data)
    
    def get_card_attribute_definition(self, bank_id: str) -> Dict:
        """
        Get card attribute definition.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing card attribute definition
        """
        return self.client.get(f"banks/{bank_id}/attribute-definitions/card")
    
    def create_or_update_card_attribute_definition(self, bank_id: str, data: Dict) -> Dict:
        """
        Create or update card attribute definition.
        
        Args:
            bank_id: Bank identifier
            data: Attribute definition data
            
        Returns:
            Dict containing created or updated attribute definition
        """
        return self.client.put(f"banks/{bank_id}/attribute-definitions/card", data=data)
    
    def delete_card_attribute_definition(self, bank_id: str, attribute_definition_id: str) -> Dict:
        """
        Delete card attribute definition.
        
        Args:
            bank_id: Bank identifier
            attribute_definition_id: Attribute definition identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/attribute-definitions/card/{attribute_definition_id}")
    
    def get_credit_card_order_status(self, bank_id: str, account_id: str) -> Dict:
        """
        Get status of Credit Card order.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            
        Returns:
            Dict containing credit card order status
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/cards/credit_card/orders")

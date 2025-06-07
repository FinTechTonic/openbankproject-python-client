"""
ATM endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class AtmEndpoints:
    """ATM-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def get_atms(self, bank_id: str, params: Optional[Dict] = None) -> Dict:
        """
        Get all ATMs at a specific bank.
        
        Args:
            bank_id: Bank identifier
            params: Optional query parameters like limit, offset, etc.
            
        Returns:
            Dict containing ATM information
        """
        return self.client.get(f"banks/{bank_id}/atms", params=params)
    
    def get_atm_by_id(self, bank_id: str, atm_id: str) -> Dict:
        """
        Get ATM by ID at a specific bank.
        
        Args:
            bank_id: Bank identifier
            atm_id: ATM identifier
            
        Returns:
            Dict containing ATM information
        """
        return self.client.get(f"banks/{bank_id}/atms/{atm_id}")
    
    def create_atm(self, bank_id: str, data: Dict) -> Dict:
        """
        Create a new ATM at a specific bank.
        
        Args:
            bank_id: Bank identifier
            data: ATM data
            
        Returns:
            Dict containing created ATM information
        """
        return self.client.post(f"banks/{bank_id}/atms", data=data)
    
    def update_atm(self, bank_id: str, atm_id: str, data: Dict) -> Dict:
        """
        Update an existing ATM at a specific bank.
        
        Args:
            bank_id: Bank identifier
            atm_id: ATM identifier
            data: Updated ATM data
            
        Returns:
            Dict containing updated ATM information
        """
        return self.client.put(f"banks/{bank_id}/atms/{atm_id}", data=data)
    
    def delete_atm(self, bank_id: str, atm_id: str) -> Dict:
        """
        Delete an ATM at a specific bank.
        
        Args:
            bank_id: Bank identifier
            atm_id: ATM identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/atms/{atm_id}")
    
    def get_atm_attributes(self, bank_id: str, atm_id: str) -> Dict:
        """
        Get attributes for an ATM.
        
        Args:
            bank_id: Bank identifier
            atm_id: ATM identifier
            
        Returns:
            Dict containing ATM attribute information
        """
        return self.client.get(f"banks/{bank_id}/atms/{atm_id}/attributes")
    
    def create_atm_attribute(self, bank_id: str, atm_id: str, data: Dict) -> Dict:
        """
        Create an attribute for an ATM.
        
        Args:
            bank_id: Bank identifier
            atm_id: ATM identifier
            data: Attribute data
            
        Returns:
            Dict containing created attribute information
        """
        return self.client.post(f"banks/{bank_id}/atms/{atm_id}/attributes", data=data)
    
    def update_atm_attribute(self, bank_id: str, atm_id: str, attribute_id: str, data: Dict) -> Dict:
        """
        Update an attribute of an ATM.
        
        Args:
            bank_id: Bank identifier
            atm_id: ATM identifier
            attribute_id: Attribute identifier
            data: Updated attribute data
            
        Returns:
            Dict containing updated attribute information
        """
        return self.client.put(f"banks/{bank_id}/atms/{atm_id}/attributes/{attribute_id}", data=data)
    
    def delete_atm_attribute(self, bank_id: str, atm_id: str, attribute_id: str) -> Dict:
        """
        Delete an attribute from an ATM.
        
        Args:
            bank_id: Bank identifier
            atm_id: ATM identifier
            attribute_id: Attribute identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/atms/{atm_id}/attributes/{attribute_id}")

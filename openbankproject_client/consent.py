"""
Consent endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class ConsentEndpoints:
    """Consent-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_consent(self, bank_id: str, data: Dict) -> Dict:
        """
        Create Consent.
        
        Args:
            bank_id: Bank identifier
            data: Consent data
            
        Returns:
            Dict containing created consent information
        """
        return self.client.post(f"banks/{bank_id}/consents", data=data)
    
    def get_consent_by_id(self, consent_id: str) -> Dict:
        """
        Get Consent By Id.
        
        Args:
            consent_id: Consent identifier
            
        Returns:
            Dict containing consent information
        """
        return self.client.get(f"consents/{consent_id}")
    
    def get_consents(self) -> Dict:
        """
        Get Consents.
        
        Returns:
            Dict containing consents information
        """
        return self.client.get("consents")
    
    def revoke_consent(self, consent_id: str) -> Dict:
        """
        Revoke Consent.
        
        Args:
            consent_id: Consent identifier
            
        Returns:
            Dict containing revocation status
        """
        return self.client.delete(f"consents/{consent_id}")
    
    def answer_consent_challenge(self, consent_id: str, data: Dict) -> Dict:
        """
        Answer Consent Challenge.
        
        Args:
            consent_id: Consent identifier
            data: Challenge answer data
            
        Returns:
            Dict containing challenge response information
        """
        return self.client.post(f"consents/{consent_id}/challenge", data=data)
    
    def get_consent_status(self, consent_id: str) -> Dict:
        """
        Get Consent Status.
        
        Args:
            consent_id: Consent identifier
            
        Returns:
            Dict containing consent status information
        """
        return self.client.get(f"consents/{consent_id}/status")
    
    def get_consent_by_bank_id_and_consent_id(self, bank_id: str, consent_id: str) -> Dict:
        """
        Get Consent By Bank Id and Consent Id.
        
        Args:
            bank_id: Bank identifier
            consent_id: Consent identifier
            
        Returns:
            Dict containing consent information
        """
        return self.client.get(f"banks/{bank_id}/consents/{consent_id}")
    
    def get_consents_by_bank_id(self, bank_id: str) -> Dict:
        """
        Get Consents By Bank Id.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing consents information
        """
        return self.client.get(f"banks/{bank_id}/consents")
    
    def update_consent_status(self, consent_id: str, data: Dict) -> Dict:
        """
        Update Consent Status.
        
        Args:
            consent_id: Consent identifier
            data: Updated status data
            
        Returns:
            Dict containing updated consent information
        """
        return self.client.put(f"consents/{consent_id}/status", data=data)

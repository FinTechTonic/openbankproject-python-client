"""
User Invitation endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class UserInvitationEndpoints:
    """User Invitation-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_user_invitation(self, bank_id: str, data: Dict) -> Dict:
        """
        Create User Invitation.
        
        Args:
            bank_id: Bank identifier
            data: User invitation data
            
        Returns:
            Dict containing created user invitation information
        """
        return self.client.post(f"banks/{bank_id}/user-invitations", data=data)
    
    def get_user_invitation(self, bank_id: str, invitation_id: str) -> Dict:
        """
        Get User Invitation.
        
        Args:
            bank_id: Bank identifier
            invitation_id: Invitation identifier
            
        Returns:
            Dict containing user invitation information
        """
        return self.client.get(f"banks/{bank_id}/user-invitations/{invitation_id}")
    
    def get_user_invitation_information(self, invitation_id: str) -> Dict:
        """
        Get User Invitation Information.
        
        Args:
            invitation_id: Invitation identifier
            
        Returns:
            Dict containing user invitation information
        """
        return self.client.get(f"user-invitations/{invitation_id}")
    
    def get_user_invitations(self, bank_id: str) -> Dict:
        """
        Get User Invitations.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing user invitations information
        """
        return self.client.get(f"banks/{bank_id}/user-invitations")

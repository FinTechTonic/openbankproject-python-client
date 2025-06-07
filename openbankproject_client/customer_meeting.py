"""
Customer Meeting endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class CustomerMeetingEndpoints:
    """Customer Meeting-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_meeting(self, bank_id: str, customer_id: str, data: Dict) -> Dict:
        """
        Create Meeting (video conference/call).
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            data: Meeting data
            
        Returns:
            Dict containing created meeting information
        """
        return self.client.post(f"banks/{bank_id}/customers/{customer_id}/meetings", data=data)
    
    def get_meeting(self, bank_id: str, customer_id: str, meeting_id: str) -> Dict:
        """
        Get Meeting.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            meeting_id: Meeting identifier
            
        Returns:
            Dict containing meeting information
        """
        return self.client.get(f"banks/{bank_id}/customers/{customer_id}/meetings/{meeting_id}")
    
    def get_meetings(self, bank_id: str, customer_id: str) -> Dict:
        """
        Get Meetings.
        
        Args:
            bank_id: Bank identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing meetings information
        """
        return self.client.get(f"banks/{bank_id}/customers/{customer_id}/meetings")

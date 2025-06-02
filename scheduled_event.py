"""
Scheduled Event endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class ScheduledEventEndpoints:
    """Scheduled Event-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_scheduled_event(self, data: Dict) -> Dict:
        """
        Create Scheduled Event.
        
        Args:
            data: Scheduled event data
            
        Returns:
            Dict containing created scheduled event information
        """
        return self.client.post("management/scheduled-events", data=data)
    
    def get_scheduled_event(self, scheduled_event_id: str) -> Dict:
        """
        Get Scheduled Event.
        
        Args:
            scheduled_event_id: Scheduled event identifier
            
        Returns:
            Dict containing scheduled event information
        """
        return self.client.get(f"management/scheduled-events/{scheduled_event_id}")
    
    def get_scheduled_events(self) -> Dict:
        """
        Get Scheduled Events.
        
        Returns:
            Dict containing scheduled events information
        """
        return self.client.get("management/scheduled-events")
    
    def update_scheduled_event(self, scheduled_event_id: str, data: Dict) -> Dict:
        """
        Update Scheduled Event.
        
        Args:
            scheduled_event_id: Scheduled event identifier
            data: Updated scheduled event data
            
        Returns:
            Dict containing updated scheduled event information
        """
        return self.client.put(f"management/scheduled-events/{scheduled_event_id}", data=data)
    
    def delete_scheduled_event(self, scheduled_event_id: str) -> Dict:
        """
        Delete Scheduled Event.
        
        Args:
            scheduled_event_id: Scheduled event identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"management/scheduled-events/{scheduled_event_id}")

"""
WebUi Props endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class WebUiPropsEndpoints:
    """WebUi Props-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_web_ui_props(self, data: Dict) -> Dict:
        """
        Create WebUiProps.
        
        Args:
            data: WebUiProps data
            
        Returns:
            Dict containing created WebUiProps information
        """
        return self.client.post("management/webui_props", data=data)
    
    def get_web_ui_props(self) -> Dict:
        """
        Get WebUiProps.
        
        Returns:
            Dict containing WebUiProps information
        """
        return self.client.get("management/webui_props")
    
    def delete_web_ui_props(self, web_ui_props_id: str) -> Dict:
        """
        Delete WebUiProps.
        
        Args:
            web_ui_props_id: WebUiProps identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"management/webui_props/{web_ui_props_id}")

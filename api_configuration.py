"""
API Configuration endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class ApiConfigurationEndpoints:
    """API Configuration-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def get_api_configuration(self) -> Dict:
        """
        Get API Configuration.
        
        Returns:
            Dict containing API configuration information
        """
        return self.client.get("config")
    
    def get_api_configuration_by_host(self, host: str) -> Dict:
        """
        Get API Configuration by Host.
        
        Args:
            host: Host identifier
            
        Returns:
            Dict containing API configuration information for the specified host
        """
        return self.client.get(f"config/{host}")
    
    def update_api_configuration(self, data: Dict) -> Dict:
        """
        Update API Configuration.
        
        Args:
            data: Updated API configuration data
            
        Returns:
            Dict containing updated API configuration information
        """
        return self.client.put("config", data=data)

"""
Webhook endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class WebhookEndpoints:
    """Webhook-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_account_webhook(self, bank_id: str, account_id: str, data: Dict) -> Dict:
        """
        Create an Account Webhook.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            data: Webhook data
            
        Returns:
            Dict containing created webhook information
        """
        return self.client.post(f"banks/{bank_id}/accounts/{account_id}/webhooks", data=data)
    
    def create_bank_account_notification_webhook(self, bank_id: str, data: Dict) -> Dict:
        """
        Create bank level Account Notification Webhook.
        
        Args:
            bank_id: Bank identifier
            data: Webhook data
            
        Returns:
            Dict containing created webhook information
        """
        return self.client.post(f"banks/{bank_id}/account-notification-webhooks", data=data)
    
    def create_system_account_notification_webhook(self, data: Dict) -> Dict:
        """
        Create system level Account Notification Webhook.
        
        Args:
            data: Webhook data
            
        Returns:
            Dict containing created webhook information
        """
        return self.client.post("account-notification-webhooks", data=data)
    
    def enable_disable_account_webhook(self, bank_id: str, account_id: str, webhook_id: str, data: Dict) -> Dict:
        """
        Enable/Disable an Account Webhook.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            webhook_id: Webhook identifier
            data: Enable/disable data
            
        Returns:
            Dict containing updated webhook information
        """
        return self.client.put(f"banks/{bank_id}/accounts/{account_id}/webhooks/{webhook_id}", data=data)
    
    def get_account_webhooks(self, bank_id: str, account_id: str) -> Dict:
        """
        Get Account Webhooks.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            
        Returns:
            Dict containing webhooks information
        """
        return self.client.get(f"banks/{bank_id}/accounts/{account_id}/webhooks")

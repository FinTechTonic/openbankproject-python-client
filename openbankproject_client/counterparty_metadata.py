"""
Counterparty Metadata endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class CounterpartyMetadataEndpoints:
    """Counterparty Metadata-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def add_corporate_location_to_counterparty(self, bank_id: str, account_id: str, view_id: str, 
                                              other_account_id: str, data: Dict) -> Dict:
        """
        Add Corporate Location to Counterparty.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            data: Corporate location data
            
        Returns:
            Dict containing created corporate location information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/corporate_location",
            data=data
        )
    
    def add_counterparty_more_info(self, bank_id: str, account_id: str, view_id: str, 
                                  other_account_id: str, data: Dict) -> Dict:
        """
        Add Counterparty More Info.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            data: More info data
            
        Returns:
            Dict containing created more info information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/more_info",
            data=data
        )
    
    def add_open_corporates_url_to_counterparty(self, bank_id: str, account_id: str, view_id: str, 
                                               other_account_id: str, data: Dict) -> Dict:
        """
        Add Open Corporates URL to Counterparty.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            data: Open Corporates URL data
            
        Returns:
            Dict containing created Open Corporates URL information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/open_corporates_url",
            data=data
        )
    
    def add_image_url_to_other_bank_account(self, bank_id: str, account_id: str, view_id: str, 
                                           other_account_id: str, data: Dict) -> Dict:
        """
        Add image url to other bank account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            data: Image URL data
            
        Returns:
            Dict containing created image URL information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/image_url",
            data=data
        )
    
    def add_physical_location_to_other_bank_account(self, bank_id: str, account_id: str, view_id: str, 
                                                  other_account_id: str, data: Dict) -> Dict:
        """
        Add physical location to other bank account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            data: Physical location data
            
        Returns:
            Dict containing created physical location information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/physical_location",
            data=data
        )
    
    def add_public_alias_to_other_bank_account(self, bank_id: str, account_id: str, view_id: str, 
                                             other_account_id: str, data: Dict) -> Dict:
        """
        Add public alias to other bank account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            data: Public alias data
            
        Returns:
            Dict containing created public alias information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/public_alias",
            data=data
        )
    
    def add_url_to_other_bank_account(self, bank_id: str, account_id: str, view_id: str, 
                                     other_account_id: str, data: Dict) -> Dict:
        """
        Add url to other bank account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            data: URL data
            
        Returns:
            Dict containing created URL information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/url",
            data=data
        )
    
    def create_other_account_private_alias(self, bank_id: str, account_id: str, view_id: str, 
                                          other_account_id: str, data: Dict) -> Dict:
        """
        Create Other Account Private Alias.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            data: Private alias data
            
        Returns:
            Dict containing created private alias information
        """
        return self.client.post(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/private_alias",
            data=data
        )
    
    def get_other_account_metadata(self, bank_id: str, account_id: str, view_id: str, 
                                  other_account_id: str) -> Dict:
        """
        Get Other Account Metadata.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            
        Returns:
            Dict containing metadata information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata"
        )
    
    def get_other_account_private_alias(self, bank_id: str, account_id: str, view_id: str, 
                                       other_account_id: str) -> Dict:
        """
        Get Other Account Private Alias.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            
        Returns:
            Dict containing private alias information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/private_alias"
        )
    
    def get_public_alias_of_other_bank_account(self, bank_id: str, account_id: str, view_id: str, 
                                              other_account_id: str) -> Dict:
        """
        Get public alias of other bank account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            
        Returns:
            Dict containing public alias information
        """
        return self.client.get(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/public_alias"
        )
    
    def update_counterparty_corporate_location(self, bank_id: str, account_id: str, view_id: str, 
                                              other_account_id: str, data: Dict) -> Dict:
        """
        Update Counterparty Corporate Location.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            data: Updated corporate location data
            
        Returns:
            Dict containing updated corporate location information
        """
        return self.client.put(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/corporate_location",
            data=data
        )
    
    def update_counterparty_image_url(self, bank_id: str, account_id: str, view_id: str, 
                                     other_account_id: str, data: Dict) -> Dict:
        """
        Update Counterparty Image Url.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            data: Updated image URL data
            
        Returns:
            Dict containing updated image URL information
        """
        return self.client.put(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/image_url",
            data=data
        )
    
    def update_counterparty_more_info(self, bank_id: str, account_id: str, view_id: str, 
                                     other_account_id: str, data: Dict) -> Dict:
        """
        Update Counterparty More Info.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            data: Updated more info data
            
        Returns:
            Dict containing updated more info information
        """
        return self.client.put(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/more_info",
            data=data
        )
    
    def update_counterparty_physical_location(self, bank_id: str, account_id: str, view_id: str, 
                                            other_account_id: str, data: Dict) -> Dict:
        """
        Update Counterparty Physical Location.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            data: Updated physical location data
            
        Returns:
            Dict containing updated physical location information
        """
        return self.client.put(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/physical_location",
            data=data
        )
    
    def update_counterparty_private_alias(self, bank_id: str, account_id: str, view_id: str, 
                                         other_account_id: str, data: Dict) -> Dict:
        """
        Update Counterparty Private Alias.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            data: Updated private alias data
            
        Returns:
            Dict containing updated private alias information
        """
        return self.client.put(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/private_alias",
            data=data
        )
    
    def update_open_corporates_url_of_counterparty(self, bank_id: str, account_id: str, view_id: str, 
                                                 other_account_id: str, data: Dict) -> Dict:
        """
        Update Open Corporates Url of Counterparty.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            data: Updated Open Corporates URL data
            
        Returns:
            Dict containing updated Open Corporates URL information
        """
        return self.client.put(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/open_corporates_url",
            data=data
        )
    
    def update_public_alias_of_other_bank_account(self, bank_id: str, account_id: str, view_id: str, 
                                                other_account_id: str, data: Dict) -> Dict:
        """
        Update public alias of other bank account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            data: Updated public alias data
            
        Returns:
            Dict containing updated public alias information
        """
        return self.client.put(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/public_alias",
            data=data
        )
    
    def update_url_of_other_bank_account(self, bank_id: str, account_id: str, view_id: str, 
                                        other_account_id: str, data: Dict) -> Dict:
        """
        Update url of other bank account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            data: Updated URL data
            
        Returns:
            Dict containing updated URL information
        """
        return self.client.put(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/url",
            data=data
        )
    
    def delete_counterparty_corporate_location(self, bank_id: str, account_id: str, view_id: str, 
                                              other_account_id: str) -> Dict:
        """
        Delete Counterparty Corporate Location.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/corporate_location"
        )
    
    def delete_counterparty_image_url(self, bank_id: str, account_id: str, view_id: str, 
                                     other_account_id: str) -> Dict:
        """
        Delete Counterparty Image URL.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/image_url"
        )
    
    def delete_counterparty_open_corporates_url(self, bank_id: str, account_id: str, view_id: str, 
                                               other_account_id: str) -> Dict:
        """
        Delete Counterparty Open Corporates URL.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/open_corporates_url"
        )
    
    def delete_counterparty_physical_location(self, bank_id: str, account_id: str, view_id: str, 
                                            other_account_id: str) -> Dict:
        """
        Delete Counterparty Physical Location.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/physical_location"
        )
    
    def delete_counterparty_private_alias(self, bank_id: str, account_id: str, view_id: str, 
                                         other_account_id: str) -> Dict:
        """
        Delete Counterparty Private Alias.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/private_alias"
        )
    
    def delete_counterparty_public_alias(self, bank_id: str, account_id: str, view_id: str, 
                                        other_account_id: str) -> Dict:
        """
        Delete Counterparty Public Alias.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/public_alias"
        )
    
    def delete_more_info_of_other_bank_account(self, bank_id: str, account_id: str, view_id: str, 
                                              other_account_id: str) -> Dict:
        """
        Delete more info of other bank account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/more_info"
        )
    
    def delete_url_of_other_bank_account(self, bank_id: str, account_id: str, view_id: str, 
                                        other_account_id: str) -> Dict:
        """
        Delete url of other bank account.
        
        Args:
            bank_id: Bank identifier
            account_id: Account identifier
            view_id: View identifier
            other_account_id: Other account identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(
            f"banks/{bank_id}/accounts/{account_id}/{view_id}/other_accounts/{other_account_id}/metadata/url"
        )

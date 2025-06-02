"""
Branch endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class BranchEndpoints:
    """Branch-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_branch(self, bank_id: str, data: Dict) -> Dict:
        """
        Create Branch.
        
        Args:
            bank_id: Bank identifier
            data: Branch data
            
        Returns:
            Dict containing created branch information
        """
        return self.client.post(f"banks/{bank_id}/branches", data=data)
    
    def get_branch(self, bank_id: str, branch_id: str) -> Dict:
        """
        Get Branch.
        
        Args:
            bank_id: Bank identifier
            branch_id: Branch identifier
            
        Returns:
            Dict containing branch information
        """
        return self.client.get(f"banks/{bank_id}/branches/{branch_id}")
    
    def get_branches_for_bank(self, bank_id: str) -> Dict:
        """
        Get Branches for a Bank.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing branches information
        """
        return self.client.get(f"banks/{bank_id}/branches")
    
    def delete_branch(self, bank_id: str, branch_id: str) -> Dict:
        """
        Delete Branch.
        
        Args:
            bank_id: Bank identifier
            branch_id: Branch identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/branches/{branch_id}")

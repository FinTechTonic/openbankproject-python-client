"""
User endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class UserEndpoints:
    """User-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def get_users(self, params: Optional[Dict] = None) -> Dict:
        """
        Get all users.
        
        Args:
            params: Optional query parameters like limit, offset, etc.
            
        Returns:
            Dict containing user information
        """
        return self.client.get("users", params=params)
    
    def get_user_by_id(self, user_id: str) -> Dict:
        """
        Get user by ID.
        
        Args:
            user_id: User identifier
            
        Returns:
            Dict containing user information
        """
        return self.client.get(f"users/{user_id}")
    
    def get_current_user(self) -> Dict:
        """
        Get the current authenticated user.
        
        Returns:
            Dict containing current user information
        """
        return self.client.get("users/current")
    
    def create_user(self, data: Dict) -> Dict:
        """
        Create a new user.
        
        Args:
            data: User data including username, email, password, etc.
            
        Returns:
            Dict containing created user information
        """
        return self.client.post("users", data=data)
    
    def update_user(self, user_id: str, data: Dict) -> Dict:
        """
        Update an existing user.
        
        Args:
            user_id: User identifier
            data: Updated user data
            
        Returns:
            Dict containing updated user information
        """
        return self.client.put(f"users/{user_id}", data=data)
    
    def delete_user(self, user_id: str) -> Dict:
        """
        Delete a user.
        
        Args:
            user_id: User identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"users/{user_id}")
    
    def get_user_attributes(self, user_id: str) -> Dict:
        """
        Get attributes for a user.
        
        Args:
            user_id: User identifier
            
        Returns:
            Dict containing user attribute information
        """
        return self.client.get(f"users/{user_id}/attributes")
    
    def add_user_attribute(self, user_id: str, data: Dict) -> Dict:
        """
        Add an attribute to a user.
        
        Args:
            user_id: User identifier
            data: Attribute data
            
        Returns:
            Dict containing added attribute information
        """
        return self.client.post(f"users/{user_id}/attributes", data=data)
    
    def update_user_attribute(self, user_id: str, attribute_id: str, data: Dict) -> Dict:
        """
        Update an attribute of a user.
        
        Args:
            user_id: User identifier
            attribute_id: Attribute identifier
            data: Updated attribute data
            
        Returns:
            Dict containing updated attribute information
        """
        return self.client.put(f"users/{user_id}/attributes/{attribute_id}", data=data)
    
    def delete_user_attribute(self, user_id: str, attribute_id: str) -> Dict:
        """
        Delete an attribute from a user.
        
        Args:
            user_id: User identifier
            attribute_id: Attribute identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"users/{user_id}/attributes/{attribute_id}")
    
    def get_user_entitlements(self, user_id: str) -> Dict:
        """
        Get entitlements for a user.
        
        Args:
            user_id: User identifier
            
        Returns:
            Dict containing user entitlement information
        """
        return self.client.get(f"users/{user_id}/entitlements")
    
    def add_user_entitlement(self, user_id: str, data: Dict) -> Dict:
        """
        Add an entitlement to a user.
        
        Args:
            user_id: User identifier
            data: Entitlement data
            
        Returns:
            Dict containing added entitlement information
        """
        return self.client.post(f"users/{user_id}/entitlements", data=data)
    
    def delete_user_entitlement(self, user_id: str, entitlement_id: str) -> Dict:
        """
        Delete an entitlement from a user.
        
        Args:
            user_id: User identifier
            entitlement_id: Entitlement identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"users/{user_id}/entitlements/{entitlement_id}")
    
    def get_user_permissions(self, user_id: str) -> Dict:
        """
        Get permissions for a user.
        
        Args:
            user_id: User identifier
            
        Returns:
            Dict containing user permission information
        """
        return self.client.get(f"users/{user_id}/permissions")
    
    def add_user_permission(self, user_id: str, data: Dict) -> Dict:
        """
        Add a permission to a user.
        
        Args:
            user_id: User identifier
            data: Permission data
            
        Returns:
            Dict containing added permission information
        """
        return self.client.post(f"users/{user_id}/permissions", data=data)
    
    def delete_user_permission(self, user_id: str, permission_id: str) -> Dict:
        """
        Delete a permission from a user.
        
        Args:
            user_id: User identifier
            permission_id: Permission identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"users/{user_id}/permissions/{permission_id}")
    
    def get_user_authentication_methods(self, user_id: str) -> Dict:
        """
        Get authentication methods for a user.
        
        Args:
            user_id: User identifier
            
        Returns:
            Dict containing user authentication method information
        """
        return self.client.get(f"users/{user_id}/authentication-methods")
    
    def add_user_authentication_method(self, user_id: str, data: Dict) -> Dict:
        """
        Add an authentication method to a user.
        
        Args:
            user_id: User identifier
            data: Authentication method data
            
        Returns:
            Dict containing added authentication method information
        """
        return self.client.post(f"users/{user_id}/authentication-methods", data=data)
    
    def delete_user_authentication_method(self, user_id: str, method_id: str) -> Dict:
        """
        Delete an authentication method from a user.
        
        Args:
            user_id: User identifier
            method_id: Authentication method identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"users/{user_id}/authentication-methods/{method_id}")
    
    def get_user_customers(self, user_id: str) -> Dict:
        """
        Get customers linked to a user.
        
        Args:
            user_id: User identifier
            
        Returns:
            Dict containing user customer information
        """
        return self.client.get(f"users/{user_id}/customers")
    
    def get_user_customer_by_id(self, user_id: str, customer_id: str) -> Dict:
        """
        Get a specific customer linked to a user.
        
        Args:
            user_id: User identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing user customer information
        """
        return self.client.get(f"users/{user_id}/customers/{customer_id}")
    
    def create_user_customer(self, user_id: str, data: Dict) -> Dict:
        """
        Create a customer linked to a user.
        
        Args:
            user_id: User identifier
            data: Customer data
            
        Returns:
            Dict containing created customer information
        """
        return self.client.post(f"users/{user_id}/customers", data=data)
    
    def update_user_customer(self, user_id: str, customer_id: str, data: Dict) -> Dict:
        """
        Update a customer linked to a user.
        
        Args:
            user_id: User identifier
            customer_id: Customer identifier
            data: Updated customer data
            
        Returns:
            Dict containing updated customer information
        """
        return self.client.put(f"users/{user_id}/customers/{customer_id}", data=data)
    
    def delete_user_customer(self, user_id: str, customer_id: str) -> Dict:
        """
        Delete a customer linked to a user.
        
        Args:
            user_id: User identifier
            customer_id: Customer identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"users/{user_id}/customers/{customer_id}")
    
    def get_user_customer_links(self, user_id: str) -> Dict:
        """
        Get customer links for a user.
        
        Args:
            user_id: User identifier
            
        Returns:
            Dict containing user customer link information
        """
        return self.client.get(f"users/{user_id}/customer-links")
    
    def create_user_customer_link(self, user_id: str, data: Dict) -> Dict:
        """
        Create a customer link for a user.
        
        Args:
            user_id: User identifier
            data: Customer link data
            
        Returns:
            Dict containing created customer link information
        """
        return self.client.post(f"users/{user_id}/customer-links", data=data)
    
    def update_user_customer_link(self, user_id: str, link_id: str, data: Dict) -> Dict:
        """
        Update a customer link for a user.
        
        Args:
            user_id: User identifier
            link_id: Customer link identifier
            data: Updated customer link data
            
        Returns:
            Dict containing updated customer link information
        """
        return self.client.put(f"users/{user_id}/customer-links/{link_id}", data=data)
    
    def delete_user_customer_link(self, user_id: str, link_id: str) -> Dict:
        """
        Delete a customer link for a user.
        
        Args:
            user_id: User identifier
            link_id: Customer link identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"users/{user_id}/customer-links/{link_id}")

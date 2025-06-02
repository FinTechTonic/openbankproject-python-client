"""
Product endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class ProductEndpoints:
    """Product-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def create_product(self, bank_id: str, data: Dict) -> Dict:
        """
        Create Product.
        
        Args:
            bank_id: Bank identifier
            data: Product data
            
        Returns:
            Dict containing created product information
        """
        return self.client.post(f"banks/{bank_id}/products", data=data)
    
    def get_bank_product(self, bank_id: str, product_id: str) -> Dict:
        """
        Get Bank Product.
        
        Args:
            bank_id: Bank identifier
            product_id: Product identifier
            
        Returns:
            Dict containing product information
        """
        return self.client.get(f"banks/{bank_id}/products/{product_id}")
    
    def get_products(self, bank_id: str) -> Dict:
        """
        Get Products.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing products information
        """
        return self.client.get(f"banks/{bank_id}/products")
    
    def get_product_tree(self, bank_id: str, product_id: str) -> Dict:
        """
        Get Product Tree.
        
        Args:
            bank_id: Bank identifier
            product_id: Product identifier
            
        Returns:
            Dict containing product tree information
        """
        return self.client.get(f"banks/{bank_id}/product-tree/{product_id}")
    
    def create_product_attribute(self, bank_id: str, product_id: str, data: Dict) -> Dict:
        """
        Create Product Attribute.
        
        Args:
            bank_id: Bank identifier
            product_id: Product identifier
            data: Attribute data
            
        Returns:
            Dict containing created attribute information
        """
        return self.client.post(f"banks/{bank_id}/products/{product_id}/attribute", data=data)
    
    def update_product_attribute(self, bank_id: str, product_id: str, product_attribute_id: str, data: Dict) -> Dict:
        """
        Update Product Attribute.
        
        Args:
            bank_id: Bank identifier
            product_id: Product identifier
            product_attribute_id: Product attribute identifier
            data: Updated attribute data
            
        Returns:
            Dict containing updated attribute information
        """
        return self.client.put(f"banks/{bank_id}/products/{product_id}/attributes/{product_attribute_id}", data=data)
    
    def get_product_attribute(self, bank_id: str, product_id: str, product_attribute_id: str) -> Dict:
        """
        Get Product Attribute.
        
        Args:
            bank_id: Bank identifier
            product_id: Product identifier
            product_attribute_id: Product attribute identifier
            
        Returns:
            Dict containing attribute information
        """
        return self.client.get(f"banks/{bank_id}/products/{product_id}/attributes/{product_attribute_id}")
    
    def delete_product_attribute(self, bank_id: str, product_id: str, product_attribute_id: str) -> Dict:
        """
        Delete Product Attribute.
        
        Args:
            bank_id: Bank identifier
            product_id: Product identifier
            product_attribute_id: Product attribute identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/products/{product_id}/attributes/{product_attribute_id}")
    
    def create_product_fee(self, bank_id: str, product_id: str, data: Dict) -> Dict:
        """
        Create Product Fee.
        
        Args:
            bank_id: Bank identifier
            product_id: Product identifier
            data: Fee data
            
        Returns:
            Dict containing created fee information
        """
        return self.client.post(f"banks/{bank_id}/products/{product_id}/fee", data=data)
    
    def update_product_fee(self, bank_id: str, product_id: str, product_fee_id: str, data: Dict) -> Dict:
        """
        Update Product Fee.
        
        Args:
            bank_id: Bank identifier
            product_id: Product identifier
            product_fee_id: Product fee identifier
            data: Updated fee data
            
        Returns:
            Dict containing updated fee information
        """
        return self.client.put(f"banks/{bank_id}/products/{product_id}/fees/{product_fee_id}", data=data)
    
    def get_product_fee(self, bank_id: str, product_id: str, product_fee_id: str) -> Dict:
        """
        Get Product Fee.
        
        Args:
            bank_id: Bank identifier
            product_id: Product identifier
            product_fee_id: Product fee identifier
            
        Returns:
            Dict containing fee information
        """
        return self.client.get(f"banks/{bank_id}/products/{product_id}/fees/{product_fee_id}")
    
    def get_product_fees(self, bank_id: str, product_id: str) -> Dict:
        """
        Get Product Fees.
        
        Args:
            bank_id: Bank identifier
            product_id: Product identifier
            
        Returns:
            Dict containing fees information
        """
        return self.client.get(f"banks/{bank_id}/products/{product_id}/fees")
    
    def delete_product_fee(self, bank_id: str, product_id: str, product_fee_id: str) -> Dict:
        """
        Delete Product Fee.
        
        Args:
            bank_id: Bank identifier
            product_id: Product identifier
            product_fee_id: Product fee identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/products/{product_id}/fees/{product_fee_id}")
    
    def get_product_attribute_definition(self, bank_id: str) -> Dict:
        """
        Get Product Attribute Definition.
        
        Args:
            bank_id: Bank identifier
            
        Returns:
            Dict containing attribute definition information
        """
        return self.client.get(f"banks/{bank_id}/attribute-definitions/product")
    
    def create_or_update_product_attribute_definition(self, bank_id: str, data: Dict) -> Dict:
        """
        Create or Update Product Attribute Definition.
        
        Args:
            bank_id: Bank identifier
            data: Attribute definition data
            
        Returns:
            Dict containing created or updated attribute definition information
        """
        return self.client.put(f"banks/{bank_id}/attribute-definitions/product", data=data)
    
    def delete_product_attribute_definition(self, bank_id: str, product_attribute_definition_id: str) -> Dict:
        """
        Delete Product Attribute Definition.
        
        Args:
            bank_id: Bank identifier
            product_attribute_definition_id: Product attribute definition identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"banks/{bank_id}/attribute-definitions/product/{product_attribute_definition_id}")
    
    def delete_product_cascade(self, bank_id: str, product_id: str) -> Dict:
        """
        Delete Product Cascade.
        
        Args:
            bank_id: Bank identifier
            product_id: Product identifier
            
        Returns:
            Dict containing deletion status
        """
        return self.client.delete(f"management/banks/{bank_id}/products/{product_id}/cascade")

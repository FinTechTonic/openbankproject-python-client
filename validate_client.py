"""
Test script for validating the OpenBankProject API client functionality.

This script performs basic validation of the client structure and imports
to ensure all endpoint modules are correctly integrated.
"""

import os
import sys
import importlib
import inspect
from typing import List, Dict, Any

# Add the parent directory to the path so we can import the client
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def validate_client_structure():
    """
    Validate the overall structure of the client package.
    """
    print("Validating client structure...")
    
    # Check that all expected files exist
    required_files = [
        "__init__.py",
        "client.py",
        "auth.py",
        "errors.py",
        "examples.py",
        "README.md"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(os.path.join("openbankproject_client", file)):
            missing_files.append(file)
    
    if missing_files:
        print(f"ERROR: Missing required files: {', '.join(missing_files)}")
        return False
    
    print("✓ All required files exist")
    return True


def validate_endpoint_modules():
    """
    Validate that all endpoint modules can be imported and contain expected classes.
    """
    print("\nValidating endpoint modules...")
    
    # Get all Python files in the directory
    endpoint_files = [f for f in os.listdir("openbankproject_client") 
                     if f.endswith(".py") and f not in ["__init__.py", "client.py", "auth.py", "errors.py", "examples.py", "validate_client.py", "setup.py"]]
    
    # Try to import each module and check for endpoint class
    successful_imports = 0
    failed_imports = []
    
    for file in endpoint_files:
        module_name = file[:-3]  # Remove .py extension
        try:
            # Force reload the module to ensure we get the latest version
            if f"openbankproject_client.{module_name}" in sys.modules:
                del sys.modules[f"openbankproject_client.{module_name}"]
                
            # Import the module
            module = importlib.import_module(f"openbankproject_client.{module_name}")
            
            # Special case for webui_props module
            if module_name == "webui_props":
                if hasattr(module, "WebUiPropsEndpoints"):
                    successful_imports += 1
                    continue
            
            # Check if it contains an endpoints class
            class_name = ''.join(word.capitalize() for word in module_name.split('_')) + 'Endpoints'
            
            if hasattr(module, class_name):
                successful_imports += 1
            else:
                failed_imports.append(f"{module_name} (missing {class_name} class)")
        except Exception as e:
            failed_imports.append(f"{module_name} (error: {str(e)})")
    
    if failed_imports:
        print(f"ERROR: Failed to validate {len(failed_imports)} modules:")
        for module in failed_imports:
            print(f"  - {module}")
    else:
        print(f"✓ Successfully validated all {successful_imports} endpoint modules")
    
    return len(failed_imports) == 0


def validate_client_initialization():
    """
    Validate that the client can be initialized and contains all endpoint groups.
    """
    print("\nValidating client initialization...")
    
    try:
        from openbankproject_client import OpenBankProjectClient
        
        # Initialize client without authentication
        client = OpenBankProjectClient(base_url="https://example.com")
        
        # Get all attributes that are endpoint groups
        endpoint_groups = []
        for attr_name in dir(client):
            if not attr_name.startswith('_') and not callable(getattr(client, attr_name)):
                attr = getattr(client, attr_name)
                if hasattr(attr, '__class__') and 'Endpoints' in attr.__class__.__name__:
                    endpoint_groups.append(attr_name)
        
        print(f"✓ Client initialized with {len(endpoint_groups)} endpoint groups")
        
        # Print all endpoint groups for verification
        print("\nEndpoint groups found:")
        for group in sorted(endpoint_groups):
            print(f"  - {group}")
        
        return True
    except Exception as e:
        print(f"ERROR: Failed to initialize client: {str(e)}")
        return False


def validate_auth_methods():
    """
    Validate that authentication methods are correctly implemented.
    """
    print("\nValidating authentication methods...")
    
    try:
        from openbankproject_client import DirectLoginAuth, GatewayLoginAuth
        
        # Check DirectLoginAuth
        direct_auth = DirectLoginAuth(token="test_token")
        headers = direct_auth.get_headers()
        if 'Authorization' in headers and 'DirectLogin' in headers['Authorization']:
            print("✓ DirectLoginAuth implementation validated")
        else:
            print("ERROR: DirectLoginAuth headers not correctly formatted")
            return False
        
        # Check GatewayLoginAuth
        gateway_auth = GatewayLoginAuth(token="test_token")
        headers = gateway_auth.get_headers()
        if 'Authorization' in headers and 'GatewayLogin' in headers['Authorization']:
            print("✓ GatewayLoginAuth implementation validated")
        else:
            print("ERROR: GatewayLoginAuth headers not correctly formatted")
            return False
        
        return True
    except Exception as e:
        print(f"ERROR: Failed to validate authentication methods: {str(e)}")
        return False


def validate_error_classes():
    """
    Validate that error classes are correctly implemented.
    """
    print("\nValidating error classes...")
    
    try:
        from openbankproject_client import (
            ApiError, AuthenticationError, ResourceNotFoundError, 
            ValidationError, PermissionError, ServerError
        )
        
        # Check inheritance
        if (issubclass(AuthenticationError, ApiError) and
            issubclass(ResourceNotFoundError, ApiError) and
            issubclass(ValidationError, ApiError) and
            issubclass(PermissionError, ApiError) and
            issubclass(ServerError, ApiError)):
            print("✓ Error class hierarchy validated")
        else:
            print("ERROR: Error class hierarchy is incorrect")
            return False
        
        # Check error instantiation
        error = ApiError("Test error", 400, {"error": "test"})
        if error.message == "Test error" and error.status_code == 400:
            print("✓ Error class instantiation validated")
        else:
            print("ERROR: Error class instantiation is incorrect")
            return False
        
        return True
    except Exception as e:
        print(f"ERROR: Failed to validate error classes: {str(e)}")
        return False


def validate_client_methods():
    """
    Validate that the client's core methods are correctly implemented.
    """
    print("\nValidating client methods...")
    
    try:
        from openbankproject_client import OpenBankProjectClient
        
        client = OpenBankProjectClient(base_url="https://example.com")
        
        # Check that the client has the expected HTTP methods
        required_methods = ['get', 'post', 'put', 'delete', 'request']
        missing_methods = []
        
        for method in required_methods:
            if not hasattr(client, method) or not callable(getattr(client, method)):
                missing_methods.append(method)
        
        if missing_methods:
            print(f"ERROR: Missing required methods: {', '.join(missing_methods)}")
            return False
        
        print("✓ All required HTTP methods are implemented")
        return True
    except Exception as e:
        print(f"ERROR: Failed to validate client methods: {str(e)}")
        return False


def run_all_validations():
    """
    Run all validation checks and report overall status.
    """
    print("=== OpenBankProject API Client Validation ===\n")
    
    validations = [
        validate_client_structure(),
        validate_endpoint_modules(),
        validate_client_initialization(),
        validate_auth_methods(),
        validate_error_classes(),
        validate_client_methods()
    ]
    
    print("\n=== Validation Summary ===")
    if all(validations):
        print("✅ All validations passed successfully!")
        return True
    else:
        print("❌ Some validations failed. Please check the errors above.")
        return False


if __name__ == "__main__":
    success = run_all_validations()
    sys.exit(0 if success else 1)

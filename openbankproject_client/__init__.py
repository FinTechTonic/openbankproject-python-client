"""
OpenBankProject Client Library
=============================

This library provides a Python client for interacting with the OpenBankProject API.
It supports various authentication methods and provides a comprehensive set of
features for working with banks, accounts, transactions, and more.

Main Features
------------
- Multiple authentication methods (DirectLogin, GatewayLogin)
- Complete account management
- Transaction handling
- User and customer management
- API management and configuration
- Support for various banking operations

Quick Start
----------
To get started, first install the package:

.. code-block:: bash

    pip install openbankproject_client

Then, you can use it in your code:

.. code-block:: python

    from openbankproject_client import OpenBankProjectClient
    from openbankproject_client.auth import DirectLoginAuth

    # Create a client with DirectLogin authentication
    auth = DirectLoginAuth(
        username="your_username",
        password="your_password",
        consumer_key="your_consumer_key"
    )
    client = OpenBankProjectClient(
        base_url="https://your-obp-instance.com",
        auth=auth
    )

    # Get list of banks
    banks = client.get_banks()

For more information, see the :doc:`getting_started/quickstart` guide.

Package Structure
---------------
The package is organized into several modules:

- :mod:`auth`: Authentication utilities
- :mod:`client`: Main client implementation
- :mod:`errors`: Error handling and custom exceptions
- :mod:`extended_account`: Extended account management
- :mod:`extended_bank`: Extended bank management
- :mod:`transaction`: Transaction management
- :mod:`user`: User management
- :mod:`api_management`: API management utilities
- And many more specialized modules

For detailed documentation of each module, see the :doc:`modules` section.
"""

from .auth import DirectLoginAuth, GatewayLoginAuth, Authentication
from .client import OpenBankProjectClient
from .errors import (
    ApiError,
    AuthenticationError,
    ResourceNotFoundError,
    ValidationError,
    PermissionError,
    RateLimitError,
    ServerError,
    ErrorHandler
)

__version__ = "1.0.0"
__all__ = [
    'OpenBankProjectClient',
    'DirectLoginAuth',
    'GatewayLoginAuth',
    'Authentication',
    'ApiError',
    'AuthenticationError',
    'ResourceNotFoundError',
    'ValidationError',
    'PermissionError',
    'RateLimitError',
    'ServerError',
    'ErrorHandler'
]

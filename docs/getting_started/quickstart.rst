Quickstart Guide
===============

This guide will help you get started with the OpenBankProject Client library quickly.

Basic Usage
----------

First, install the package:

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

Authentication
-------------

The library supports multiple authentication methods:

1. DirectLogin (username/password)
2. GatewayLogin (token-based)

For more details, see the :doc:`authentication` guide.

Working with Accounts
-------------------

Here's how to work with accounts:

.. code-block:: python

    # Get private accounts at a bank
    accounts = client.get_private_accounts_at_bank("your_bank_id")

    # Get account details
    account = client.get_account("your_bank_id", "your_account_id", "owner")

    # Get account metadata
    metadata = client.get_account_metadata("your_bank_id", "your_account_id", "owner")

Working with Transactions
-----------------------

Here's how to work with transactions:

.. code-block:: python

    # Get transactions for an account
    transactions = client.get_transactions_for_account(
        "your_bank_id",
        "your_account_id",
        "owner"
    )

    # Get transaction metadata
    metadata = client.get_transaction_metadata(
        "your_bank_id",
        "your_account_id",
        "your_transaction_id",
        "owner"
    )

Error Handling
-------------

The library provides specific exception types for different error scenarios:

.. code-block:: python

    from openbankproject_client import (
        ApiError,
        AuthenticationError,
        ResourceNotFoundError,
        ValidationError,
        PermissionError,
        ServerError
    )

    try:
        client.get_banks()
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
    except ResourceNotFoundError as e:
        print(f"Resource not found: {e}")
    except ValidationError as e:
        print(f"Validation error: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except ServerError as e:
        print(f"Server error: {e}")
    except ApiError as e:
        print(f"API error: {e}")

For more detailed information about specific features, please refer to the API documentation. 
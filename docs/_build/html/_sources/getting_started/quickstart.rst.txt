Quickstart Guide
===============

This guide will help you get started with the OpenBankProject Client quickly.

Basic Usage
----------

First, import and initialize the client:

.. code-block:: python

    from openbankproject_client import OpenBankProjectClient

    # Initialize the client
    client = OpenBankProjectClient(
        base_url="https://your-obp-instance.com",
        consumer_key="your-consumer-key",
        consumer_secret="your-consumer-secret"
    )

Authentication
-------------

Authenticate using OAuth1:

.. code-block:: python

    # Authenticate
    client.authenticate(
        username="your-username",
        password="your-password"
    )

Working with Accounts
-------------------

Get a list of accounts:

.. code-block:: python

    # Get all accounts
    accounts = client.get_accounts()

    # Get a specific account
    account = client.get_account_by_id("account-id")

Working with Transactions
-----------------------

Get transactions for an account:

.. code-block:: python

    # Get transactions
    transactions = client.get_transactions(
        bank_id="bank-id",
        account_id="account-id",
        view_id="owner"
    )

Error Handling
-------------

The client raises specific exceptions for different error cases:

.. code-block:: python

    from openbankproject_client.errors import OBPError, AuthenticationError

    try:
        client.authenticate(username="user", password="pass")
    except AuthenticationError as e:
        print(f"Authentication failed: {e}")
    except OBPError as e:
        print(f"API error: {e}")

For more detailed information about specific features, please refer to the API documentation. 
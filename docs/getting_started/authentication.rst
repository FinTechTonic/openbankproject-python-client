Authentication
=============

The OpenBankProject Client uses OAuth1 for authentication. This guide explains how to authenticate with the API.

OAuth1 Authentication
-------------------

The client supports OAuth1 authentication with the following methods:

Direct Authentication
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from openbankproject_client import OpenBankProjectClient

    client = OpenBankProjectClient(
        base_url="https://your-obp-instance.com",
        consumer_key="your-consumer-key",
        consumer_secret="your-consumer-secret"
    )

    # Authenticate with username and password
    client.authenticate(
        username="your-username",
        password="your-password"
    )

Token-based Authentication
~~~~~~~~~~~~~~~~~~~~~~~~

If you already have OAuth tokens:

.. code-block:: python

    client = OpenBankProjectClient(
        base_url="https://your-obp-instance.com",
        consumer_key="your-consumer-key",
        consumer_secret="your-consumer-secret",
        oauth_token="your-oauth-token",
        oauth_token_secret="your-oauth-token-secret"
    )

Getting Consumer Keys
-------------------

To get consumer keys for your application:

1. Log in to your OpenBankProject instance
2. Go to the API Explorer
3. Register a new application
4. Note down the consumer key and secret

Security Best Practices
---------------------

* Never commit consumer keys or secrets to version control
* Use environment variables or a secure configuration management system
* Rotate credentials regularly
* Use the minimum required permissions for your application

Example with Environment Variables
-------------------------------

.. code-block:: python

    import os
    from openbankproject_client import OpenBankProjectClient

    client = OpenBankProjectClient(
        base_url=os.environ["OBP_BASE_URL"],
        consumer_key=os.environ["OBP_CONSUMER_KEY"],
        consumer_secret=os.environ["OBP_CONSUMER_SECRET"]
    )

Error Handling
-------------

The client provides specific exceptions for authentication errors:

.. code-block:: python

    from openbankproject_client.errors import AuthenticationError, OBPError

    try:
        client.authenticate(username="user", password="pass")
    except AuthenticationError as e:
        print(f"Authentication failed: {e}")
    except OBPError as e:
        print(f"API error: {e}") 
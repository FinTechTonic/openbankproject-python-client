# OpenBankProject Client

A Python client library for interacting with the OpenBankProject API. This library provides a comprehensive set of features for working with banks, accounts, transactions, and more.

## Features

- Multiple authentication methods (DirectLogin, GatewayLogin)
- Complete account management
- Transaction handling
- User and customer management
- API management and configuration
- Support for various banking operations

## Installation

```bash
pip install openbankproject_client
```

For development installation with documentation dependencies:

```bash
pip install -e ".[docs]"
```

## Quick Start

```python
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
```

## Documentation

For detailed documentation, including API reference and examples, visit our [documentation site](https://openbankproject-client.readthedocs.io/).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

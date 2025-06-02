"""
Usage examples for the OpenBankProject API Client.

This module provides examples of how to use the OpenBankProject API client
for common banking operations.
"""

from openbankproject_client import OpenBankProjectClient


def authenticate_with_direct_login():
    """
    Example of authenticating with DirectLogin.
    """
    # Initialize client with DirectLogin credentials
    client = OpenBankProjectClient(
        base_url="https://api.openbankproject.com",
        api_version="v5.1.0",
        username="your_username",
        password="your_password",
        consumer_key="your_consumer_key"
    )
    
    # Authenticate (this happens automatically on the first API call)
    client.authenticate()
    
    print("Successfully authenticated with DirectLogin")
    return client


def authenticate_with_gateway_login():
    """
    Example of authenticating with GatewayLogin.
    """
    # Initialize client with GatewayLogin token
    client = OpenBankProjectClient(
        base_url="https://api.openbankproject.com",
        api_version="v5.1.0",
        gateway_login_token="your_gateway_login_token"
    )
    
    print("Successfully initialized with GatewayLogin token")
    return client


def get_banks_example(client):
    """
    Example of getting a list of banks.
    """
    # Get all banks
    banks = client.extended_bank.get_banks()
    
    print(f"Found {len(banks.get('banks', []))} banks")
    for bank in banks.get('banks', []):
        print(f"Bank ID: {bank.get('id')}, Name: {bank.get('full_name')}")
    
    return banks


def get_accounts_example(client, bank_id):
    """
    Example of getting accounts for a bank.
    """
    # Get private accounts for a bank
    accounts = client.extended_account.get_private_accounts_at_bank(bank_id)
    
    print(f"Found {len(accounts.get('accounts', []))} accounts at bank {bank_id}")
    for account in accounts.get('accounts', []):
        print(f"Account ID: {account.get('id')}, Label: {account.get('label')}")
    
    return accounts


def get_transactions_example(client, bank_id, account_id):
    """
    Example of getting transactions for an account.
    """
    # Get transactions for an account (using owner view)
    transactions = client.transaction.get_transactions_for_account(bank_id, account_id, "owner")
    
    print(f"Found {len(transactions.get('transactions', []))} transactions for account {account_id}")
    for transaction in transactions.get('transactions', [])[:5]:  # Show first 5 transactions
        print(f"Transaction ID: {transaction.get('id')}, Amount: {transaction.get('details', {}).get('value', {}).get('amount')}")
    
    return transactions


def create_transaction_request_example(client, bank_id, account_id, counterparty_id):
    """
    Example of creating a transaction request.
    """
    # Create a transaction request to a counterparty
    transaction_data = {
        "to": {
            "bank_id": bank_id,
            "account_id": counterparty_id
        },
        "value": {
            "currency": "EUR",
            "amount": "10.00"
        },
        "description": "Test payment",
        "challenge_type": ""
    }
    
    try:
        result = client.transaction_request.create_transaction_request_counterparty(
            bank_id, account_id, "owner", transaction_data
        )
        print(f"Transaction request created with ID: {result.get('id')}")
        return result
    except Exception as e:
        print(f"Error creating transaction request: {str(e)}")
        return None


def create_counterparty_example(client, bank_id, account_id):
    """
    Example of creating a counterparty.
    """
    # Create a new counterparty
    counterparty_data = {
        "name": "Test Counterparty",
        "other_account_routing_scheme": "IBAN",
        "other_account_routing_address": "DE89370400440532013000",
        "other_account_secondary_routing_scheme": "BIC",
        "other_account_secondary_routing_address": "DEUTDEFF",
        "other_bank_routing_scheme": "BIC",
        "other_bank_routing_address": "DEUTDEFF",
        "other_branch_routing_scheme": "",
        "other_branch_routing_address": "",
        "is_beneficiary": True
    }
    
    try:
        result = client.counterparty.create_counterparty_explicit(
            bank_id, account_id, "owner", counterparty_data
        )
        print(f"Counterparty created with ID: {result.get('counterparty_id')}")
        return result
    except Exception as e:
        print(f"Error creating counterparty: {str(e)}")
        return None


def get_customer_example(client, bank_id, customer_id):
    """
    Example of getting customer information.
    """
    try:
        customer = client.customer.get_customer(bank_id, customer_id)
        print(f"Customer: {customer.get('customer_number')}, Name: {customer.get('legal_name')}")
        return customer
    except Exception as e:
        print(f"Error getting customer: {str(e)}")
        return None


def create_meeting_example(client, bank_id, customer_id):
    """
    Example of creating a customer meeting.
    """
    meeting_data = {
        "provider_id": "video_conference_provider",
        "purpose_id": "customer_onboarding",
        "date": "2023-12-01T10:00:00Z",
        "details": "Initial customer onboarding meeting"
    }
    
    try:
        result = client.customer_meeting.create_meeting(bank_id, customer_id, meeting_data)
        print(f"Meeting created with ID: {result.get('meeting_id')}")
        return result
    except Exception as e:
        print(f"Error creating meeting: {str(e)}")
        return None


def create_consent_example(client, bank_id):
    """
    Example of creating a consent.
    """
    consent_data = {
        "consent_type": "account_access",
        "network_id": "network_id",
        "phone_number": "+44123456789",
        "email": "user@example.com",
        "consumer_id": "consumer_id",
        "valid_from": "2023-01-01T00:00:00Z",
        "time_to_live": 3600,
        "everything": False,
        "views": ["owner"],
        "accounts": [{"bank_id": bank_id, "account_id": "account_id"}],
        "entitlements": {
            "entitlements": [
                {"bank_id": bank_id, "role_name": "CanGetCustomer"}
            ]
        }
    }
    
    try:
        result = client.consent.create_consent(bank_id, consent_data)
        print(f"Consent created with ID: {result.get('consent_id')}")
        return result
    except Exception as e:
        print(f"Error creating consent: {str(e)}")
        return None


def create_standing_order_example(client, bank_id, account_id):
    """
    Example of creating a standing order.
    """
    standing_order_data = {
        "name": "Monthly Rent",
        "start_date": "2023-01-01",
        "end_date": "2023-12-31",
        "frequency": "Monthly",
        "amount": "1000.00",
        "currency": "EUR",
        "to": {
            "bank_id": bank_id,
            "account_id": "target_account_id"
        }
    }
    
    try:
        result = client.standing_order.create_standing_order(bank_id, account_id, "owner", standing_order_data)
        print(f"Standing order created with ID: {result.get('standing_order_id')}")
        return result
    except Exception as e:
        print(f"Error creating standing order: {str(e)}")
        return None


def create_direct_debit_example(client, bank_id, account_id):
    """
    Example of creating a direct debit.
    """
    direct_debit_data = {
        "customer_id": "customer_id",
        "user_id": "user_id",
        "counterparty_id": "counterparty_id",
        "date_signed": "2023-01-01",
        "date_starts": "2023-01-15",
        "date_expires": "2023-12-31",
        "active": True
    }
    
    try:
        result = client.direct_debit.create_direct_debit(bank_id, account_id, "owner", direct_debit_data)
        print(f"Direct debit created with ID: {result.get('direct_debit_id')}")
        return result
    except Exception as e:
        print(f"Error creating direct debit: {str(e)}")
        return None


def error_handling_example():
    """
    Example of handling API errors.
    """
    from openbankproject_client import (
        ApiError, AuthenticationError, ResourceNotFoundError, 
        ValidationError, PermissionError, ServerError
    )
    
    client = OpenBankProjectClient(
        base_url="https://api.openbankproject.com",
        api_version="v5.1.0",
        username="invalid_username",
        password="invalid_password",
        consumer_key="invalid_key"
    )
    
    try:
        # This will fail due to invalid credentials
        client.extended_bank.get_banks()
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
    except Exception as e:
        print(f"Unexpected error: {e}")


def main():
    """
    Run all examples.
    """
    # Replace these with valid values for your environment
    bank_id = "your_bank_id"
    account_id = "your_account_id"
    customer_id = "your_customer_id"
    counterparty_id = "your_counterparty_id"
    
    # Authenticate
    client = authenticate_with_direct_login()
    
    # Run examples
    get_banks_example(client)
    get_accounts_example(client, bank_id)
    get_transactions_example(client, bank_id, account_id)
    create_counterparty_example(client, bank_id, account_id)
    create_transaction_request_example(client, bank_id, account_id, counterparty_id)
    get_customer_example(client, bank_id, customer_id)
    create_meeting_example(client, bank_id, customer_id)
    create_consent_example(client, bank_id)
    create_standing_order_example(client, bank_id, account_id)
    create_direct_debit_example(client, bank_id, account_id)
    
    # Error handling example
    error_handling_example()


if __name__ == "__main__":
    main()

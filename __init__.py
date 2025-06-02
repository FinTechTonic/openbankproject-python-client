"""
OpenBankProject API Client

This module provides a comprehensive Python client for interacting with the OpenBankProject API v5.1.0.
"""

from .client import OpenBankProjectClient
from .auth import DirectLoginAuth, GatewayLoginAuth
from .errors import (
    ApiError, AuthenticationError, ResourceNotFoundError, 
    ValidationError, PermissionError, ServerError
)

__all__ = [
    'OpenBankProjectClient',
    'DirectLoginAuth',
    'GatewayLoginAuth',
    'ApiError',
    'AuthenticationError',
    'ResourceNotFoundError',
    'ValidationError',
    'PermissionError',
    'ServerError'
]

__version__ = '2.0.0'

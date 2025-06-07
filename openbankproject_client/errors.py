"""
Error handling utilities for the OpenBankProject API Client.
"""

from typing import Dict, Optional, Any


class ApiError(Exception):
    """Base exception for OpenBankProject API errors."""
    
    def __init__(self, message: str, status_code: Optional[int] = None, detail: Optional[Dict] = None):
        """
        Initialize the exception.
        
        Args:
            message: Error message
            status_code: HTTP status code (if applicable)
            detail: Additional error details
        """
        self.message = message
        self.status_code = status_code
        self.detail = detail
        super().__init__(self.message)
    
    def __str__(self) -> str:
        """Return string representation of the error."""
        if self.status_code:
            return f"{self.message} (Status: {self.status_code})"
        return self.message


class AuthenticationError(ApiError):
    """Exception raised for authentication errors."""
    pass


class ResourceNotFoundError(ApiError):
    """Exception raised when a resource is not found."""
    pass


class ValidationError(ApiError):
    """Exception raised for validation errors."""
    pass


class PermissionError(ApiError):
    """Exception raised for permission errors."""
    pass


class RateLimitError(ApiError):
    """Exception raised when rate limit is exceeded."""
    pass


class ServerError(ApiError):
    """Exception raised for server errors."""
    pass


class ErrorHandler:
    """Utility class for handling API errors."""
    
    @staticmethod
    def handle_error_response(response: Any) -> None:
        """
        Handle error responses from the API.
        
        Args:
            response: Response object from requests library
            
        Raises:
            AuthenticationError: For authentication errors (401)
            PermissionError: For permission errors (403)
            ResourceNotFoundError: For not found errors (404)
            ValidationError: For validation errors (400)
            RateLimitError: For rate limit errors (429)
            ServerError: For server errors (5xx)
            ApiError: For other errors
        """
        if not hasattr(response, 'status_code'):
            raise ApiError("Invalid response object")
        
        try:
            error_detail = response.json() if response.text else {}
        except:
            error_detail = {"error": response.text}
        
        status_code = response.status_code
        
        if status_code == 400:
            raise ValidationError(
                f"Bad request: {error_detail.get('error', 'Invalid request')}",
                status_code=status_code,
                detail=error_detail
            )
        elif status_code == 401:
            raise AuthenticationError(
                f"Authentication failed: {error_detail.get('error', 'Invalid credentials')}",
                status_code=status_code,
                detail=error_detail
            )
        elif status_code == 403:
            raise PermissionError(
                f"Permission denied: {error_detail.get('error', 'Insufficient permissions')}",
                status_code=status_code,
                detail=error_detail
            )
        elif status_code == 404:
            raise ResourceNotFoundError(
                f"Resource not found: {error_detail.get('error', 'The requested resource does not exist')}",
                status_code=status_code,
                detail=error_detail
            )
        elif status_code == 429:
            raise RateLimitError(
                f"Rate limit exceeded: {error_detail.get('error', 'Too many requests')}",
                status_code=status_code,
                detail=error_detail
            )
        elif 500 <= status_code < 600:
            raise ServerError(
                f"Server error: {error_detail.get('error', 'Internal server error')}",
                status_code=status_code,
                detail=error_detail
            )
        else:
            raise ApiError(
                f"API error: {error_detail.get('error', 'Unknown error')}",
                status_code=status_code,
                detail=error_detail
            )

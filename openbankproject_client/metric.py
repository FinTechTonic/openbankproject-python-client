"""
Metric endpoints for the OpenBankProject API Client.
"""

from typing import Dict, List, Optional, Union, Any


class MetricEndpoints:
    """Metric-related API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the endpoint group.
        
        Args:
            client: OpenBankProjectClient instance
        """
        self.client = client
    
    def get_metrics(self) -> Dict:
        """
        Get Metrics.
        
        Returns:
            Dict containing metrics information
        """
        return self.client.get("metrics")
    
    def get_metrics_top_apis(self) -> Dict:
        """
        Get Top APIs.
        
        Returns:
            Dict containing top APIs metrics information
        """
        return self.client.get("metrics/top-apis")
    
    def get_metrics_top_consumers(self) -> Dict:
        """
        Get Top Consumers.
        
        Returns:
            Dict containing top consumers metrics information
        """
        return self.client.get("metrics/top-consumers")
    
    def get_metrics_top_warehouse_calls(self) -> Dict:
        """
        Get Top Warehouse Calls.
        
        Returns:
            Dict containing top warehouse calls metrics information
        """
        return self.client.get("metrics/top-warehouse-calls")
    
    def get_metrics_api_explorer(self) -> Dict:
        """
        Get API Explorer Metrics.
        
        Returns:
            Dict containing API explorer metrics information
        """
        return self.client.get("metrics/api-explorer")
    
    def get_metrics_connector_metrics(self) -> Dict:
        """
        Get Connector Metrics.
        
        Returns:
            Dict containing connector metrics information
        """
        return self.client.get("metrics/connector-metrics")
    
    def get_metrics_aggregate(self) -> Dict:
        """
        Get Aggregate Metrics.
        
        Returns:
            Dict containing aggregate metrics information
        """
        return self.client.get("metrics/aggregate")

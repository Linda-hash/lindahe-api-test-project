import requests
import logging
from typing import Optional, Dict, Any

class APIClient:
    """A reusable client for making HTTP requests to an API"""
    def __init__(self, base_url: str, log_level = logging.INFO):
        """Initialize the API client with base URL and logging level"""
        self.base_url = base_url
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> requests.Response:
        """Internal method to handle all HTTP requests"""
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"Making {method} request to {url}")
        
        if headers:
            self.session.headers.update(headers)

        # Make the HTTP request with optional parameters and JSON body  
        response = self.session.request(
            method=method,
            url=url,
            params=params,
            json=json,
            **kwargs
        )
        # Log response details
        self.logger.info(f"Response status code: {response.status_code}")
        self.logger.info(f"Response body: {response.text}")
        
        return response

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        """Make a GET request to the specified endpoint"""
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        """Make a POST request to the specified endpoint"""
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs) -> requests.Response:
        """Make a PUT request to the specified endpoint"""
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """Make a DELETE request to the specified endpoint"""
        return self._request("DELETE", endpoint, **kwargs)

    def patch(self, endpoint: str, **kwargs) -> requests.Response:
        """Make a PATCH request to the specified endpoint"""
        return self._request("PATCH", endpoint, **kwargs)
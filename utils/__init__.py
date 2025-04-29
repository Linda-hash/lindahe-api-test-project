# utils/__init__.py
"""
This package contains utility modules for API testing:
- api_client: Handles all API requests
- helpers: Contains helper functions for testing
"""

# 可以暴露主要的工具类/函数，方便导入
from .api_client import APIClient
from .helpers import load_test_data, assert_response

__all__ = ['APIClient', 'load_test_data', 'assert_response']
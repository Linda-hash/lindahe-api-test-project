# tests/__init__.py
"""
This module contains all API test cases for the project.
"""

# 可以定义测试相关的共享常量
API_VERSION = "v1"
DEFAULT_TIMEOUT = 10  # seconds

# 或者可以添加一些共享的pytest fixtures
import pytest

@pytest.fixture
def shared_fixture():
    """An example shared fixture available to all tests in this package"""
    return {"shared": "data"}
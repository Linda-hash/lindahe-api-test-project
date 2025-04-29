import json
from typing import Any, Dict

def load_test_data(file_path: str) -> Dict[str, Any]:
    """Load test data from JSON file"""
    with open(file_path, 'r') as file:
        return json.load(file)

def assert_response(
    response,
    expected_status_code: int = 200,
    expected_data: Dict[str, Any] = None
) -> None:
    """Assert common response checks including status code and response data"""
    assert response.status_code == expected_status_code
    if expected_data:
        assert response.json() == expected_data


def validate_response_data(actual_data, expected_data, search_key):
    """Recursively validate response data structure and content"""
    # Validate dictionary structure and content recursively
    if isinstance(actual_data, dict) and isinstance(expected_data, dict):
        for key in expected_data:
            if key not in actual_data:
                assert False, f"Key {key} cannot be found in actual data"
            validate_response_data(actual_data[key], expected_data[key], search_key)
        # verify if actual_data contains extra keys
        for key in actual_data:
            if key not in expected_data:
                assert False, f"actual data contains extra {key}"

    # Validate list structure and content recursively
    elif isinstance(actual_data, list) and isinstance(expected_data, list):
        assert len(actual_data) == len(expected_data)
        for actual_item, expected_item in zip(actual_data, expected_data):
            validate_response_data(actual_item, expected_item, search_key)
    
    # Validate individual values
    else:
        # Special handling for string values with search key
        if isinstance(actual_data, str) and isinstance(expected_data, str) and search_key:
            if search_key.lower() in str(expected_data).lower():
                assert search_key.lower() in actual_data.lower(), f"{search_key} not found in {actual_data}"
            else:
                assert actual_data == expected_data, f"data can't match, expect: {expected_data},actual: {actual_data}"
        else:
            assert actual_data == expected_data, f"data can't match, expected {expected_data}, actual {actual_data}"


import requests

# ... existing code ...

def validate_image_url(url: str) -> bool:
    """Validate if an image URL returns 200 OK"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        print(f"Content Length: {len(response.content)}")
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        return False
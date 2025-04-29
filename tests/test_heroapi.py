import pytest
import re
from utils.helpers import load_test_data, assert_response, validate_response_data, validate_image_url

@pytest.mark.usefixtures("api_client")
class TestHeroAPI:
    """Test cases for hero API"""
    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        """Initialize test setup with API client and test data"""
        self.client = api_client
        self.test_data = load_test_data("test_data/test_data.json")

    
    def test_search_empty_name(self):
        """Test search functionality with empty name parameter"""
        response = self.client.get("/search/{name}")
        assert_response(response, expected_status_code=200)
        assert len(response.json()) > 0

    @pytest.mark.parametrize("name,expected_status_code", [
        ("batman", 200),
        ("man", 200),
        ("@#$%", 400),
        ("123456", 200),
        ("a" * 1000, 414),
        ("abcdefg", 200),
        ("BATMAN", 200)
    ])
    def test_search_by_name(self, name, expected_status_code):
        """Test search functionality with various name inputs"""
        response = self.client.get(f"/search/{name}")
        assert_response(response, expected_status_code)
    
        if expected_status_code == 200:
            actual_data = response.json()
            lower_name = name.lower()
            results = actual_data.get("results", [])

        # Compile regex pattern to match either whole word or partial match          
        pattern = re.compile(rf'\b{re.escape(lower_name)}\b|{re.escape(lower_name)}', re.IGNORECASE)
        for result in results:
            assert pattern.search(result["name"]), f"Expected '{lower_name}' in '{result['name']}'"          
            
            # Validate against expected data if available           
            expected_data = self.test_data.get(lower_name)
            if expected_data:
                expected_results_count = len(expected_data.get("results", []))
                assert len(results) >= expected_results_count, f"Expected at least {expected_results_count} results"
                validate_response_data(actual_data, expected_data, lower_name)

    
    @pytest.mark.parametrize("access_token, expected_status_code", [
        ("dlajfdosaiuwq", 400),
        ("", 401)
         ])
    def test_access_token(self, access_token, expected_status_code):
        """Test API access with different token scenarios"""
        response = self.client.get(f"/{access_token}/search/batman")
        assert_response(response, expected_status_code)

    def test_image_urls(self):
        """Test if all image URLs in the response are valid"""
        response = self.client.get("/search/batman")
        assert_response(response, expected_status_code=200)
    
        data = response.json()
        results = data.get("results", [])
    
        for result in results:
            image_url = result.get("image")
            print(f"Image URL: {print(f"URL: {url}")}")
            assert image_url, f"Image URL is missing in result: {result}"
        
            # if image_url is a dic, extract the url
            if isinstance(image_url, dict):
                url = image_url.get('url')
                assert url, f"URL is missing in image object: {image_url}"
            else:
                url = image_url
            assert validate_image_url(url), f"Invalid image URL: {url}"

        



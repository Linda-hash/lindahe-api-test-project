import pytest
import os
from dotenv import load_dotenv
from utils.api_client import APIClient
from datetime import datetime

load_dotenv()

@pytest.fixture(scope="session")
def api_client():
    """Fixture to provide an API client instance for testing"""
    access_token = "b6f918c29272bbef1e3fa540c500a51e"
    base_url = os.getenv("API_BASE_URL", f"https://superheroapi.com/api/{access_token}")
    return APIClient(base_url)

# @pytest.fixture
# def auth_headers(api_client):
#     # Example of authentication flow
#     login_data = {
#         "username": "testuser",
#         "password": "testpass"
#     }
#     response = api_client.post("/auth/login", json=login_data)
#     token = response.json().get("token")
#     return {"Authorization": f"Bearer {token}"}

def pytest_configure(config):
    """Configure pytest settings and generate report names"""
    # Create Report directory if it doesn't exist
    report_dir = os.path.join(os.path.dirname(__file__), "report")
    os.makedirs(report_dir, exist_ok=True)
    
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    # Get test file names from command-line arguments
    test_files = config.getoption("file_or_dir")
    if test_files:
        test_script_names = []
        for test_file in test_files:
            # check if the test_file is a file or a directory
            if os.path.isfile(test_file):
                file_name = os.path.basename(test_file)
                # check if the file name starts with "test_" and ends with ".py"
                if file_name.startswith("test_") and file_name.endswith(".py"):
                    test_script_name = os.path.splitext(file_name)[0]
                    test_script_names.append(test_script_name)
            # check if the test_file is a directory
            elif os.path.isdir(test_file):
                for root, dirs, files in os.walk(test_file):
                    for file in files:
                        if file.startswith("test_") and file.endswith(".py"):
                            test_script_name = os.path.splitext(file)[0]
                            test_script_names.append(test_script_name)
        if test_script_names:
            # if there are test files, combine their names with "_"
            combined_name = "_".join(test_script_names)
        else:
            # if there are no test files, use the default names
            combined_name = "default_test"
    else:
        combined_name = "default_test"
    """Configure pytest settings and generate report names"""
    report_name = f"{combined_name}_{now}.html"
    config.option.htmlpath = os.path.join(report_dir, report_name)
    config.option.alluredir = os.path.join(report_dir, f"allure-results_{now}")
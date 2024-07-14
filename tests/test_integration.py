import pytest
from playwright.sync_api import Page
import json

FRONTEND_URL = "http://127.0.0.1:53921"  # Replace with your frontend URL
BACKEND_URL = "http://127.0.0.1:54010/greet"

def get_backend_response():
    import requests
    response = requests.get(BACKEND_URL)
    data = json.loads(response.text.strip())
    message = data["message"]
    return message

def test_frontend_backend_integration(page: Page):
    expected_message = get_backend_response()
    page.goto(FRONTEND_URL)
    frontend_message = page.text_content("//h1[normalize-space()='Hello from the Backend!']")
    assert frontend_message == expected_message, f"Expected '{expected_message}', but got '{frontend_message}'"

test_data = [
    ("1","Hello from the Backend!")
]
@pytest.mark.parametrize("sl_no,expected_message",test_data)
def test_frontend_content(page:Page,sl_no: str, expected_message: str):
    page.goto(FRONTEND_URL)
    frontend_message = page.text_content("//h1[normalize-space()='Hello from the Backend!']")
    assert frontend_message == expected_message, f"Expected '{expected_message}', but got '{frontend_message}'"

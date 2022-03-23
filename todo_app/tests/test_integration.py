import os
import pytest
import requests
from todo_app import app
from dotenv import load_dotenv, find_dotenv


@pytest.fixture
def client():
    
    # using the .env.test configuration file
    file_path = find_dotenv(".env.test")
    load_dotenv(file_path, override=True)
    
    # creating a new app
    test_app = app.create_app()

    # using the app to create a test_client that is used in the tests
    with test_app.test_client() as client:
        yield client


def test_index_page(monkeypatch, client):
    # Arrange
    monkeypatch.setattr(requests, "request", get_lists_stub) # line 30 trello_items

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200
    assert "test card" in response.data.decode()


class StubResponse:
    ok = True

    def __init__(self, fake_response_data) -> None:
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data


def get_lists_stub(method, url, headers = {}):
    test_board_id = os.environ.get("BOARD_ID")
    fake_response_data = None
    print(url)
    print(f"https://api.trello.com/1/boards/{test_board_id}/lists")
    if url.startswith(f"https://api.trello.com/1/boards/{test_board_id}/lists"):
        fake_response_data = [
            {
                "id": "XYZ789",
                "name": "NOT STARTED",
                "cards": [{"id": "789", "name": "test card"}],
            }
        ]
        return StubResponse(fake_response_data)

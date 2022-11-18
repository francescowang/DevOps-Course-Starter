import os
import pytest
import requests
from todo_app import app
from dotenv import load_dotenv, find_dotenv
from todo_app.data.mongodb_items import MongoDB_Items


import mongomock
@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client


def test_index_page(client):
    # Arrange
    MongoDB_Items().add_mongo_card("test card")
    
    # Act
    response = client.get("/")
    
    # Assert
    assert response.status_code == 200
    assert "test card" in response.data.decode()


"""
Tests
Adding new items
Deleting new items
Marking items as 'doing' or 'completed' or moving the item back to 'not started'
"""
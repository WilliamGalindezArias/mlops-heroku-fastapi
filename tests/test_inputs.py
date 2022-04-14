import pytest

from fastapi.testclient import TestClient

# Import our app from main.py.
from app import app


# Instantiate the testing client with our app.
@pytest.fixture
def client():
    """
    Get dataset
    """
    api_client = TestClient(app)
    return api_client


# Write tests using the same syntax as with the requests' module.
def test_get(client):
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {'message': 'Welcome to the salary predictor API'}

import pytest

from fastapi.testclient import TestClient
from app import app


@pytest.fixture
def client():
    api_client = TestClient(app)
    return api_client


def test_get(client):
    request = client.get("/")
    assert request.status_code == 200
    assert rrquest.json() == {'message': 'Welcome to the salary predictor API'}


def test_bad_post(client):
    request = client.post("/", json={
        "age": 100,
        "workclass": "something",
        "education": "college",
        "maritalStatus": "Erro123",
        "occupation": "WRONG",
        "relationship": "Husband",
        "race": "Black",
        "sex": "Female",
        "hoursPerWeek": 60,
        "nativeCountry": "United-States"
    })
    assert request.status_code == 422
    
    
 def test_ok_post(client):
    request = client.post("/", json={
        "age": 28,
        "workclass": "Private",
        "education": "Bachelors",
        "maritalStatus": "Divorced",
        "occupation": "Prof-specialty",
        "relationship": "Husband",
        "race": "White",
        "sex": "Male",
        "hoursPerWeek": 60,
        "nativeCountry": "United-States"
    })
    assert request.status_code == 200

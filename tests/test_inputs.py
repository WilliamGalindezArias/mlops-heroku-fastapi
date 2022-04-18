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
    assert request.json() == {'message': 'Welcome to the salary predictor API'}


def test_bad_post(client):
    request = client.post("/predictions", json={
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
    request = client.post("/predictions", json={
        "age": 39,
        "fnlgt": 77516,
        "workclass": "State-gov",
        "education": "Bachelors",
        "education_num": 13,
        "marital_status": "Never-married",
        "occupation": "Adm-clerical",
        "relationship": "Not-in-family",
        "race": "White",
        "sex": "Male",
        "capital_gain": 2174,
        "capital_loss": 0,
        "hours_per_week": 40,
        "native_country": "United-States"
    })
    assert request.status_code == 200


def small_than_salary(client):
    request = client.post("/predictions", json={
        "age": 39,
        "fnlgt": 77516,
        "workclass": "State-gov",
        "education": "Bachelors",
        "education_num": 13,
        "marital_status": "Never-married",
        "occupation": "Adm-clerical",
        "relationship": "Not-in-family",
        "race": "White",
        "sex": "Male",
        "capital_gain": 2174,
        "capital_loss": 0,
        "hours_per_week": 40,
        "native_country": "United-States"
    })
    assert request.status_code == 200
    assert request.json() =={'Predicted Salary': '<=50K'}


def greater_than_salary(client):
    request = client.post("/predictions", json={
        "age": 32,
        "fnlgt": 77516,
        "workclass": "Private",
        "education": "Bachelors",
        "education_num": 20,
        "marital_status": "Never-married",
        "occupation": "Exec-managerial",
        "relationship": "Husband",
        "race": "White",
        "sex": "Male",
        "capital_gain": 2174,
        "capital_loss": 0,
        "hours_per_week": 60,
        "native_country": "United-States"
    })
    assert request.status_code == 200
    assert request.json() == {'Predicted Salary': '>50K'}
"""
This script does a POST test to a deployed application

Author: William
April 2022
"""

import requests

URL = "https://devops-ml.herokuapp.com/predictions"
data = {
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
        "native_country": "United-States"}
    

post_request = requests.post(URL, json=data)
print(f"Response code: {post_request.status_code}")
print(f"Response body: {post_request.json()}")

assert post_request.status_code == 200


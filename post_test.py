"""
This script does a POST test to a deployed application

Author: William
April 2022
"""

import requests

URL = "https://devops-ml.herokuapp.com/"
data = {
        "age": 39,
        "workclass": "State-gov",
        "education": "Bachelors",
        "maritalStatus": "Married-civ-spouse",
        "occupation": "Adm-clerical",
        "relationship": "Not-in-family",
        "race": "White",
        "sex": "Male",
        "hoursPerWeek": 40,
        "nativeCountry": "United-States"
    }

post_request = requests.post(URL, json=data)

assert post_request.status_code == 200

print(f"Response code: {post_request.status_code}")
print(f"Response body: {post_request.json()}")

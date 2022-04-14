"""
Author: William Arias
Date: April 2022
FastAPI application to run queries and get predictions
"""

from pydantic import BaseModel
from fastapi import FastAPI
from src.ml.data import process_data
from src.ml.model import inference
import pandas as pd
import configparser
import pickle as pkl
import logging
import joblib
import os

config = configparser.ConfigParser()
config.read('config.ini')

model_path = config['DEFAULT']['MODEL_PATH']


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
logger = logging.getLogger()

# DVC on Heroku
if "DYNO" in os.environ and os.path.isdir(".dvc"):
    os.system("dvc config core.no_scm true")
    os.system("dvc remote add -df s3-bucket s3://mlops-app/census/")
    if os.system("dvc pull") != 0:
        exit("dvc pull failed")
    os.system("rm -r .dvc .apt/usr/lib/dvc")


class CensusInputData(BaseModel):
    """ Input type used to query the model via the API and get predictions """
    age: int
    workclass: str
    education: str
    education_num: int
    marital_status: str
    occupation: str
    relationship: str
    race: str
    sex: str
    capital_gain: int
    capital_loss: int
    hours_per_week: int
    native_country: str


app = FastAPI(title="Census data")


@app.on_event("startup")
def startup_event():
    """
    Load model on startup to speed up execution
    """

    with open("models/classifier.pkl", "rb") as model_file:
        model = joblib.load(model_file)

    return model


@app.get("/")
async def home():
    return {'message': 'Welcome to the salary predictor API'}


@app.post("/predictions")
async def prediction(input_data: CensusInputData):
    with open("models/classifier.pkl", 'rb') as f:
        encoder, lb, model = pkl.load(f)

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]

    input_df = pd.DataFrame(
        {k: v for k, v in input_data.dict().items()}, index=[0]
    )
    input_df.columns = [_.replace('_', '-') for _ in input_df.columns]

    X, _, _, _ = process_data(
        X=input_df,
        label=None,
        training=False,
        categorical_features=cat_features,
        encoder=encoder,
        lb=lb,
    )

    prediction = inference(model, X)
    y = lb.inverse_transform(prediction)[0]
    logger.info(f"SUCCESS: Predicted Salary: {y}")

    return {"Predicted Salary": y}

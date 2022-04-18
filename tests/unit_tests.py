import pandas as pd
import pytest
from src.ml.data import process_data


@pytest.fixture
def data():
    """
    Get dataset
    """
    df = pd.read_csv("data/census_cleaned.csv", skipinitialspace=True)
    df = process_data(df)
    return df


def test_null(data):
    """
    No Null values contained in the dataset
    """
    assert data.shape == data.dropna().shape


def test_shape(data):
    """
        Shape of the dataset
    """
    assert data.shape == (32561, 15)


def test_process_data():
    """
    test preprocessing outputs.
    """
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
    df = pd.read_csv("data/cleaned/census_cleaned.csv")
    X, Y, _, _ = process_data(
                df,
                categorical_features=cat_features,
                label="salary", encoder=None, lb=None, training=True)

    assert X.shape[0] == df.shape[0]



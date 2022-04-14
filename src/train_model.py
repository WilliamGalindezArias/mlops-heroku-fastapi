# Model training 
# Script to train machine learning model.

from sklearn.model_selection import train_test_split
from ml.data import process_data
from ml import model

import pandas as pd
import pickle as pkl


data_path = "../data/census.csv"
model_path = "../models/classifier.pkl"
metrics_path = "../models/metrics_slice.csv"


def save_model(model_path, encoder, lb, clf):
    with open(model_path, "wb") as f:
        pkl.dump([encoder, lb, clf], f)


# 1. Load data
data = pd.read_csv(data_path, index_col=0, skipinitialspace=True)

# 2. Train-test split.
train, test = train_test_split(data, test_size=0.20)

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

# 3. Process data
X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label='salary', training=True
)

X_test, y_test, _, _ = process_data(
    test, categorical_features=cat_features, label="salary", training=False, encoder=encoder, lb=lb
)

# 4. Train and save a model

clf = model.train_model(X_train, y_train)

save_model(model_path=model_path, encoder=encoder, lb=lb, clf=clf)

# 5. Inference

training_predictions = model.inference(clf, X_train)
testing_predictions = model.inference(clf, X_test)

# 6. Metrics

precision, recall, f_beta = model.compute_model_metrics(y_test, testing_predictions)

# 7. Metrics by slice

model.compute_metrics_by_slice(
    clf=clf,
    encoder=encoder,
    lb=lb,
    df=test,
    target="salary",
    cat_columns=cat_features,
    output_path=metrics_path
)


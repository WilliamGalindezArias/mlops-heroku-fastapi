# Model Card

- Author: William Arias
- Created: April 2022


## Model Details

Implemented Random Forest Classifier. Dataset is census data obtained [here](https://archive.ics.uci.edu/ml/datasets/census+income) with 32561 observations
The model classifies based on demographic data if a person belongs to  a group of people earning above or below $50K.

The model is trained on 80% of dataset, 20% is reserved for tests.


There are also predictions done on categorical slices of data. The results are stored to:
`models/metrics_slice.csv`


## Intended Use
Education and experimentation as part of Udacity NanoDegree Program in DevOps for ML
This project semi-automates some steps in the Model Creation and testing
Leverages [DVC](dvc.org) to keep track of the datasets versions


## Training Data
Census data used to train the model can be found under `data/census_cleaned.csv`

## Notebooks
There is an EDA step in a jupyter notebook, where duplicates in the dataset where removed to avoid to some extent BIAS in the learning algorithm
and cleaning of blank spaces in the csv header

## Testing Data
20% of the data is used as testing. Data was obtained spliting it using sklearn functions for it 



## Intended Use
That is a trianing project for Udacity nano degree program.
The intention is to automate CI/CD for Machine Learning project with FastAPI and Heroku.
I use DVC to record pipeline stages and metrics. DVC with S3 is used to store artifacts remotely.


## Training Data
Census data are provided with the project under `data/census.csv`


## Evaluation Data
20% of the census data is used to validate the model


## Metrics

Testing  metrics are displayed while training the algorithm and results obtained:
```Precision: 0.6800276434001382 

Recall :0.6108007448789572 

f_beta :0.643557880967953 

```

And slices have metrics stored for every feature:
 ```
 column,category,precision,recall,f1
 education,Bachelors,0.7453703703703703,0.7301587301587301,0.7376861397479954
```

## Ethical Considerations
Demographics and predictions that involve human bias require extra care and consideration to avoid discrimination due to biased datasets

## Recommendations and Caveats
More parameter tunning and training can be don eto improve model performance. It wasn't done here given the intent of the project which was
learning CI/CD Principles for ML 

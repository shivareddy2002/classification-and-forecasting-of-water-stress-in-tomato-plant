import os
import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

MODEL_FOLDER = "models"

def preprocess_data(df, scaler=None, expected_columns=None):
    df.fillna(0, inplace=True)
    if "y" in df.columns and "status" in df.columns:
        df = df.drop(["y", "status"], axis=1)
    if expected_columns:
        df = df[expected_columns]
    if scaler is None:
        scaler = MinMaxScaler()
        X = scaler.fit_transform(df.values)
        joblib.dump(scaler, f"{MODEL_FOLDER}/scaler.joblib")
        joblib.dump(list(df.columns), f"{MODEL_FOLDER}/columns.joblib")
    else:
        X = scaler.transform(df.values)
    return X

def load_scaler():
    scaler = joblib.load(f"{MODEL_FOLDER}/scaler.joblib")
    expected_columns = joblib.load(f"{MODEL_FOLDER}/columns.joblib")
    return scaler, expected_columns

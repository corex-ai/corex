import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import dump
from logger import logger

def train_model():
    df = pd.read_csv("training_data.csv")
    X = df.drop("signal", axis=1)
    y = df["signal"]

    model = RandomForestClassifier()
    model.fit(X, y)

    dump(model, "corex_model.joblib")
    logger.info("✅ Model trained and saved successfully.")

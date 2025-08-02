from joblib import load
from logger import logger

def predict_signal(price_data):
    model = load("corex_model.joblib")
    prediction = model.predict([price_data])
    logger.info(f"AI Prediction done for input: {price_data}")
    return prediction[0]

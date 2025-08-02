import pickle
import os

def predict_signal(prices):
    # trained_model.pkl ka path
    model_path = os.path.join(os.path.dirname(__file__), 'trained_model.pkl')

    # Model load karo
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    # Predict karo
    prediction = model.predict([prices])
    return prediction[0]

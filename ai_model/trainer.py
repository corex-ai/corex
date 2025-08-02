import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle
import os

def train_model():
    # Load training data
    data_path = os.path.join(os.path.dirname(__file__), '../training_data.csv')
    df = pd.read_csv(data_path)

    # Features = price1 to price5
    X = df[['price1', 'price2', 'price3', 'price4', 'price5']]
    y = df['signal']

    # Train model
    model = DecisionTreeClassifier()
    model.fit(X, y)

    # Save model
    model_path = os.path.join(os.path.dirname(__file__), 'trained_model.pkl')
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

    print("✅ AI Model Trained and Saved Successfully!")

# Run if executed directly
if __name__ == "__main__":
    train_model()

from flask import Flask, jsonify, request
from signal_engine import generate_signal
from ai_model.trainer import train_model
from ai_model.predictor import predict_signal
from logger import logger

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "🟢 CoreX Signal Engine running!"})

@app.route('/signal', methods=['POST'])
def signal():
    data = request.get_json()
    price_data = data.get("price_data", [])
    signal_result = generate_signal(price_data)
    return jsonify(signal_result)

@app.route('/train_model')
def train():
    try:
        train_model()
        return jsonify({"message": "✅ AI Model trained successfully."})
    except Exception as ex:
        logger.error(f"❌ Training failed: {ex}")
        return jsonify({"error": str(ex)}), 500

@app.route('/ai_signal', methods=['POST'])
def ai_signal():
    data = request.get_json()
    price_data = data.get("price_data", [])

    if not price_data or len(price_data) < 5:
        return jsonify({"error": "Need at least 5 prices"}), 400

    try:
        prediction = predict_signal(price_data)
        return jsonify({"ai_signal": prediction})
    except Exception as ex:
        logger.error(f"❌ AI prediction failed: {ex}")
        return jsonify({"error": str(ex)}), 500

# Final production server using waitress
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)

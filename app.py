from flask import Flask, jsonify, request
from signal_engine import generate_signal
from ai_model.trainer import train_model
from ai_model.predictor import predict_signal
from logger import logger

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "✅ CoreX Signal Engine running!"})

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
    except Exception as e:
        logger.error(f"❌ Training failed: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/ai_signal', methods=['POST'])
def ai_signal():
    data = request.get_json()
    price_data = data.get("price_data", [])

    if not price_data or len(price_data) < 5:
        return jsonify({"error": "Need at least 5 prices"}), 400

    try:
        prediction = predict_signal(price_data)
        return jsonify({
            "ai_signal": prediction
        })
    except Exception as e:
        logger.error(f"❌ AI prediction failed: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

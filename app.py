from flask import Flask, jsonify, request
import os
from signal_engine import generate_signal
from signal_engine.price_fetcher import fetch_price_data
from ai_model.trainer import train_model  # ✅ Naya import
from logger import logger

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 CoreX AI Trading System is live and running!"

@app.route('/signal', methods=['POST'])
def signal():
    data = request.get_json()
    price_data = data.get('price_data', [])

    logger.info(f"📥 Incoming price data: {price_data}")

    if not price_data or len(price_data) < 2:
        return jsonify({"error": "Need at least 2 prices"}), 400

    result = generate_signal(price_data)

    logger.info(f"📤 Final signal response: {result}")

    return jsonify(result)

@app.route('/live_signal', methods=['GET'])
def live_signal():
    price_data = fetch_price_data()
    result = generate_signal(price_data)
    return jsonify(result)

# ✅ Naya AI Model Train Route
@app.route('/train_model', methods=['GET'])
def trigger_training():
    try:
        train_model()
        return jsonify({"message": "✅ AI Model trained successfully."})
    except Exception as e:
        logger.error(f"❌ Training error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

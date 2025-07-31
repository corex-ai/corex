from flask import Flask, jsonify, request
import os
from signal_engine import generate_signal

app = Flask(__name__)

@app.route('/')
def home():
    return '🚀 CoreX AI Trading System is live and running!'

@app.route('/signal', methods=['POST'])
def signal():
    data = request.get_json()
    price_data = data.get('price_data', [])
    
    if not price_data or len(price_data) < 2:
        return jsonify({"error": "Need at least 2 prices"}), 400
    
    signal = generate_signal(price_data)
    return jsonify({"signal": signal})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # Restarted for redeploy

from flask import Flask, jsonify
from signal_engine import generate_signal
from signal_engine.price_fetcher import fetch_price_data

app = Flask(__name__)

@app.route("/")
def index():
    try:
        price_data = fetch_price_data()
        signal = generate_signal(price_data)
        return jsonify(signal)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '🚀 CoreX AI Trading System is live and running on Railway!'

if __name__ == '__main__':
    app.run(debug=True)
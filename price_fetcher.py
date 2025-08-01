import requests

def fetch_price_data(symbol="BTCUSDT", interval="1m", limit=15):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract close prices from candles
        close_prices = [float(entry[4]) for entry in data]
        return close_prices

    except Exception as e:
        print(f"❌ Error fetching price data: {e}")
        # Fallback dummy data
        return [100, 102, 101, 103, 104, 105, 106, 105, 104, 102, 101, 100, 98, 97, 96]

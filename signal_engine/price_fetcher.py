from logger import logger
import requests

def fetch_price_data(symbol="bitcoin"):
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart"
        params = {
            "vs_currency": "usd",
            "days": "1",
            "interval": "minute"
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        prices = data.get("prices", [])
        price_data = [round(p[1], 2) for p in prices[-100:] if p]
        return price_data if price_data else fallback_prices()

    except Exception as e:
        logger.error(f"❌ Error fetching price for {symbol}: {e}")
        return fallback_prices()

def fallback_prices():
    return [100, 102, 101, 103, 104, 105, 106, 105, 104, 102, 101, 100, 98, 97, 96]

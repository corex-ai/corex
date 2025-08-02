from .indicators import calculate_indicators
from .price_fetcher import fetch_price_data

def generate_signal(price_data):
    indicators = calculate_indicators(price_data)
    return indicators

from .indicators import calculate_indicators

def generate_signal(price_data):
    indicators = calculate_indicators(price_data)
    return indicators

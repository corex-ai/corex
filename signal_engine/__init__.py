def generate_signal(price_data):
    """
    Dummy signal generator – future me AI & strategy yaha add hoga.
    """
    if price_data[-1] > price_data[-2]:
        return "BUY"
    elif price_data[-1] < price_data[-2]:
        return "SELL"
    else:
        return "HOLD"

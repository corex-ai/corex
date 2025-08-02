def calculate_indicators(price_data):
    if not price_data or len(price_data) < 3:
        return {"signal": "HOLD", "confidence": 0.0, "explanation": "Not enough data."}

    sma = sum(price_data[-3:]) / 3
    last_price = price_data[-1]

    if last_price > sma:
        return {"signal": "BUY", "confidence": 0.7, "explanation": f"Price ({last_price}) > SMA ({sma})"}
    elif last_price < sma:
        return {"signal": "SELL", "confidence": 0.7, "explanation": f"Price ({last_price}) < SMA ({sma})"}
    else:
        return {"signal": "HOLD", "confidence": 0.5, "explanation": "Price equals SMA"}

from .indicators import sma, ema, rsi

def generate_signal(price_data):
    """
    AI-Style signal generator with confidence score.
    """

    if len(price_data) < 15:
        return {"signal": "HOLD", "confidence": 0}

    sma_value = sma(price_data, period=5)
    ema_value = ema(price_data, period=5)
    rsi_value = rsi(price_data, period=14)

    score = 0

    if rsi_value < 30:
        score += 1
    elif rsi_value > 70:
        score -= 1

    if price_data[-1] > ema_value:
        score += 1
    elif price_data[-1] < ema_value:
        score -= 1

    if price_data[-1] > sma_value:
        score += 1
    elif price_data[-1] < sma_value:
        score -= 1

    if score >= 2:
        return {"signal": "BUY", "confidence": abs(score) / 3}
    elif score <= -2:
        return {"signal": "SELL", "confidence": abs(score) / 3}
    else:
        return {"signal": "HOLD", "confidence": abs(score) / 3}

from .indicators import sma, ema, rsi  # ✅ Yeh top line hai

def generate_signal(price_data):
    if len(price_data) < 15:
        return {
            "signal": "HOLD",
            "confidence": 0.0,
            "explanation": "Not enough data to generate signal"
        }

    sma_value = sma(price_data, period=5)
    ema_value = ema(price_data, period=5)
    rsi_value = rsi(price_data, period=14)

    if rsi_value is None:
        return {
            "signal": "HOLD",
            "confidence": 0.0,
            "explanation": "RSI calculation failed"
        }

    explanation = ""
    confidence = 0.5  # base confidence

    if rsi_value < 30 and price_data[-1] > ema_value:
        explanation = f"RSI is {rsi_value} (oversold) and price is above EMA ({ema_value})"
        confidence += 0.2
        return {
            "signal": "BUY",
            "confidence": round(confidence, 2),
            "explanation": explanation
        }

    elif rsi_value > 70 and price_data[-1] < ema_value:
        explanation = f"RSI is {rsi_value} (overbought) and price is below EMA ({ema_value})"
        confidence += 0.2
        return {
            "signal": "SELL",
            "confidence": round(confidence, 2),
            "explanation": explanation
        }

    else:
        explanation = f"RSI is {rsi_value}, price near EMA ({ema_value}), no clear signal"
        return {
            "signal": "HOLD",
            "confidence": round(confidence, 2),
            "explanation": explanation
        }

from .indicators import sma, ema, rsi  # ✅ Yeh top line hai

def generate_signal(price_data):
    if len(price_data) < 15:
        return "HOLD"

    sma_value = sma(price_data, period=5)
    ema_value = ema(price_data, period=5)
    rsi_value = rsi(price_data, period=14)

    if rsi_value is None:
        return "HOLD"

    if rsi_value < 30 and price_data[-1] > ema_value:
        return "BUY"
    elif rsi_value > 70 and price_data[-1] < ema_value:
        return "SELL"
    else:
        return "HOLD"

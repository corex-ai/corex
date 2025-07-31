def sma(data, period=5):
    if len(data) < period:
        return None
    return sum(data[-period:]) / period

def ema(data, period=5):
    if len(data) < period:
        return None
    k = 2 / (period + 1)
    ema_val = data[0]
    for price in data[1:]:
        ema_val = (price * k) + (ema_val * (1 - k))
    return ema_val

def rsi(data, period=14):
    if len(data) < period + 1:
        return None
    gains, losses = [], []
    for i in range(1, period + 1):
        diff = data[-i] - data[-i - 1]
        if diff >= 0:
            gains.append(diff)
        else:
            losses.append(abs(diff))
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period
    if avg_loss == 0:
        return 100
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

import numpy as np
import pandas as pd
from ta.trend import MACD, SMAIndicator
from ta.momentum import RSIIndicator

def generate_trading_signals(data):
    short_ma = SMAIndicator(data['Close'], window=10).sma_indicator()
    long_ma = SMAIndicator(data['Close'], window=50).sma_indicator()
    macd = MACD(data['Close']).macd_diff()
    rsi = RSIIndicator(data['Close']).rsi()
    
    signals = pd.DataFrame(index=data.index)
    signals['short_ma'] = short_ma
    signals['long_ma'] = long_ma
    signals['macd'] = macd
    signals['rsi'] = rsi
    signals['signal'] = 0.0

    # Example trading logic
    signals['signal'][10:] = np.where(signals['short_ma'][10:] > signals['long_ma'][10:], 1.0, 0.0)
    signals['positions'] = signals['signal'].diff()

    return signals

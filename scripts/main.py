import yfinance as yf
import numpy as np
import pandas as pd
from sentiment_analysis import get_market_sentiment
from technical_analysis import calculate_moving_average, plot_price_and_moving_averages

def generate_trading_signals(data):
    short_ma = calculate_moving_average(data['Close'], 10)
    long_ma = calculate_moving_average(data['Close'], 50)
    
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    signals['short_ma'] = short_ma
    signals['long_ma'] = long_ma
    signals['signal'][10:] = np.where(signals['short_ma'][10:] > signals['long_ma'][10:], 1.0, 0.0)   
    signals['positions'] = signals['signal'].diff()
    return signals

if __name__ == "__main__":
    sentiment_score = get_market_sentiment()
    gold_data = yf.download('GC=F', start='2021-01-01', end='2024-01-01')
    data = gold_data[['Close']]
    signals = generate_trading_signals(data)
    plot_price_and_moving_averages(data, window_sizes=[10, 50])
    print("Sentiment Score:", sentiment_score)
    print("Trading Signals:", signals)

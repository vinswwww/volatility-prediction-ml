import yfinance as yf
import pandas as pd
import numpy as np

def download_prices(tickers, start, end):
    data = yf.download(tickers, start=start, end=end)
    return data["Close"]

def compute_returns(prices):
    return prices.pct_change().dropna()

def compute_log_returns(prices):
    return np.log(prices / prices.shift(1)).dropna()

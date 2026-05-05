import pandas as pd
import numpy as np

def create_vol_features(vol_series):
    df = pd.DataFrame()

    df["vol"] = vol_series
    df["vol_lag1"] = vol_series.shift(1)
    df["vol_lag5"] = vol_series.shift(5)
    df["vol_lag10"] = vol_series.shift(10)
    df["vol_lag21"] = vol_series.shift(21)

    df["target"] = vol_series.shift(-1)

    return df.dropna()

def compute_realized_volatility(returns, window=21, annualize=True):
    realized_vol = returns.rolling(window=window).std()
    if annualize:
        realized_vol = realized_vol * np.sqrt(252)
    return realized_vol.dropna()

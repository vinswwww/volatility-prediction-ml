import numpy as np
from scipy.stats import norm

def compute_dynamic_var(pred_vol, alpha=0.05):
    daily_vol = pred_vol / np.sqrt(252)
    var = norm.ppf(alpha) * daily_vol
    return var

def compute_rolling_var(returns, window=21, alpha=0.05):
    rolling_vol = returns.rolling(window).std()
    var = norm.ppf(alpha) * rolling_vol
    return var

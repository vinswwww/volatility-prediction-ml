# Volatility Forecasting and Dynamic Value-at-Risk with Machine Learning

## Overview

This project develops an end-to-end volatility forecasting and risk management pipeline using daily SPY and VIX market data. The workflow combines traditional econometric volatility models with modern machine learning approaches to predict future realized volatility and apply those forecasts to Dynamic Value-at-Risk (VaR) estimation.

The project is organized into modular research-style notebooks covering:

1. Data preparation and realized volatility construction  
2. Volatility forecasting model development  
3. Dynamic VaR backtesting and risk evaluation  

The goal is to compare whether machine learning models can improve volatility forecasting accuracy and downstream risk measurement relative to classical benchmark methods.

---

# Project Objectives

The project focuses on three main questions:

- Can machine learning models outperform traditional volatility benchmarks?
- How do ensemble models compare with econometric approaches such as GARCH(1,1)?
- Do improved volatility forecasts lead to better Value-at-Risk calibration?

---

# Data

The project uses daily market data for:

- **SPY** — S&P 500 ETF
- **VIX** — CBOE Volatility Index

Features are constructed from rolling realized volatility estimates and lagged volatility dynamics.

---

# Feature Engineering

The forecasting models use lagged realized volatility features:

| Feature | Description |
|---|---|
| `vol_lag1` | 1-day lagged volatility |
| `vol_lag5` | 5-day lagged volatility |
| `vol_lag10` | 10-day lagged volatility |
| `vol_lag21` | 21-day lagged volatility |

Additional processing includes:

- Rolling annualized realized volatility
- Time-ordered train/test split
- Alignment of forecasting and VaR evaluation periods

---

# Models Implemented

## Benchmark Models

### Baseline Volatility Forecast
Uses previous-day realized volatility as the forecast.

### GARCH(1,1)
Classical econometric volatility model implemented with the `arch` package.

---

## Machine Learning Models

### Ridge Regression
Linear regularized benchmark model.

### Random Forest
Bagging-based ensemble regression model.

### Extra Trees
Randomized tree ensemble for nonlinear volatility dynamics.

### XGBoost
Gradient boosting model optimized for time-series volatility prediction.

### Stacking Ensemble
Combines:
- Ridge
- Random Forest
- Extra Trees
- XGBoost

using Ridge regression as the final meta-model.

---

# Hyperparameter Tuning

Time-series-aware cross-validation is implemented using:

- `TimeSeriesSplit`
- `RandomizedSearchCV`

for tuning XGBoost hyperparameters, including:

- number of estimators
- tree depth
- learning rate
- subsampling ratio

This avoids look-ahead bias common in financial forecasting tasks.

---

# Evaluation Metrics

Forecasting performance is evaluated out-of-sample using:

| Metric | Purpose |
|---|---|
| RMSE | Penalizes larger forecasting errors |
| MAE | Measures average absolute prediction error |

Models are compared on the same out-of-sample test period.

---

# Dynamic Value-at-Risk Application

The project extends volatility forecasting into a practical risk management application.

Predicted volatility forecasts are converted into:

- Dynamic 1-day 5% Value-at-Risk estimates

These forecasts are benchmarked against:

- Rolling Historical VaR

using violation-rate backtesting.

---

# VaR Backtesting

The project evaluates:

- Violation rate
- Distance from theoretical 5% violation target
- Number of VaR breaches

This allows comparison between:
- model-based Dynamic VaR
- rolling historical benchmark VaR

---

# Project Structure

```text
volatility-prediction/
│
├── data/
│   ├── prices.csv
│   ├── returns.csv
│   ├── model_data.csv
│   ├── model_predictions.csv
│   ├── model_comparison.csv
│   ├── model_predictions.csv
│   └── var_backtest_series.csv
│   └── var_comparison.csv
│
├── notebooks/
│   ├── 01_data_setup.ipynb
│   ├── 02_modeling.ipynb
│   └── 03_application_var.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_utils.py
│   ├── features.py
│   ├── models.py
│   ├── evaluation.py
│   └── var.py
│
├── figures/
│   ├── dynamic_var_vs_benchmark.png
│   └── volatility_forecast.png
│
├── requirements.txt
│
└── README.md
```

---

# Workflow

## Notebook 1 — Data Preparation

- Load SPY and VIX data
- Compute realized volatility
- Create lagged volatility features
- Export modeling datasets

---

## Notebook 2 — Volatility Forecasting

- Train benchmark and ML models
- Tune XGBoost with time-series CV
- Compare RMSE and MAE
- Evaluate GARCH benchmark
- Save out-of-sample forecasts

---

## Notebook 3 — Dynamic VaR

- Construct Dynamic VaR from predicted volatility
- Compare against rolling historical VaR
- Perform VaR backtesting
- Visualize VaR breaches
- Export final backtesting outputs

---

# Technologies Used

- Python
- pandas
- numpy
- scikit-learn
- XGBoost
- arch
- matplotlib

---

# Key Concepts

This project applies concepts from:

- Financial econometrics
- Time-series forecasting
- Ensemble machine learning
- Volatility modeling
- Risk management
- Value-at-Risk backtesting

---

# Author

**Shawn Wen**  
Applied Mathematics — Data Science & Financial Economics

University of Washington
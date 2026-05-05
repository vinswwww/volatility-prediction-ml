# Volatility Prediction with Machine Learning

## Overview

This project builds a volatility prediction pipeline using financial time series data (SPY & VIX).

It compares traditional econometric models with modern machine learning methods.

## Models Implemented

* Baseline (historical volatility)
* Random Forest
* GARCH(1,1)
* XGBoost
* Ridge Regression
* Extra Trees
* Stacking Ensemble

## Features

* Lagged volatility features (1, 5, 10, 21 days)
* Rolling realized volatility
* Train/test split for time series

## Results

Models are evaluated using:

* RMSE
* MAE

## Optional Extension

Includes a volatility trading strategy using predicted volatility.

## Tech Stack

* Python (pandas, numpy)
* scikit-learn
* XGBoost
* arch (GARCH)
* matplotlib

## Structure

```
data/
notebooks/
src/
```

## Author

Shaobo Wen

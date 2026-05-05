from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from xgboost import XGBRegressor

def get_ridge():
    return Ridge(alpha=1.0)

def get_rf():
    return RandomForestRegressor(
        n_estimators=300,
        max_depth=5,
        random_state=42
    )

def get_extra():
    return ExtraTreesRegressor(
        n_estimators=500,
        max_depth=6,
        min_samples_leaf=5,
        random_state=42
    )

def get_xgb():
    return XGBRegressor(
        n_estimators=300,
        learning_rate=0.03,
        max_depth=3,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="reg:squarederror",
        random_state=42
    )

# Description: Short example for Measuring Error in Time Series Forecasting with Python.


import logging

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sktime.performance_metrics.forecasting import (
    mean_absolute_error,
    mean_absolute_scaled_error,
    mean_squared_error,
)

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)


# Example Time Series
y_true = np.array([10, 12, 13, 14, 15])
y_pred_naive = np.roll(y_true, 1)  # Shift values by 1 as naive forecast
y_pred_naive[0] = y_true[0]  # No forecast for the first observation

# Calculate MAE for Naive Forecast
mae_naive = mean_absolute_error(y_true[1:], y_pred_naive[1:])
logger.info(f"MAE (Naive Forecast): {mae_naive:.4f}")


def simple_moving_average(y, window_size):
    return np.convolve(y, np.ones(window_size) / window_size, mode="valid")


# Example Time Series
y_true = np.array([10, 12, 14, 16, 18, 20])
window_size = 2

y_pred_sma = simple_moving_average(y_true, window_size)

# Align y_true and predictions
y_true_trim = y_true[window_size - 1 :]

mae_sma = mean_absolute_error(y_true_trim, y_pred_sma)
logger.info(f"MAE (Simple Moving Average): {mae_sma:.4f}")

# Example Time Series
y_true = np.array([10, 12, 15, 18, 20])
y_pred = np.array([11, 13, 14, 17, 21])
# Calculate MAE
mae = mean_absolute_error(y_true, y_pred)
logger.info(f"Mean Absolute Error (MAE): {mae}")

# Calculate MSE
mse = mean_squared_error(y_true, y_pred)
logger.info(f"Mean Squared Error (MSE): {mse}")


def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


# Example Time Series
y_true = np.array([10, 12, 15, 18, 20])
y_pred = np.array([11, 13, 14, 17, 21])

# Calculate MAPE
mape = mean_absolute_percentage_error(y_true, y_pred)
logger.info(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")

# Calculate MASE
mase = mean_absolute_scaled_error(y_true, y_pred, y_train=y_true)
logger.info(f"Mean Absolute Scaled Error (MASE): {mase}")

df.dropna(inplace=True)
mae = mean_absolute_error(df["weight"], df["naive_weight"])
mse = mean_squared_error(df["weight"], df["naive_weight"])
logger.info(f"Naive Forecast - MAE: {mae:.2f}, MSE: {mse:.2f}")

"""Forecast error metrics and plotting using Polars and DuckDB.

sklearn.metrics (MSE, MAE, MAPE) are replaced with equivalent DuckDB SQL aggregates.
"""

import duckdb
import polars as pl
import matplotlib.pyplot as plt
from pathlib import Path


def calculate_error_metrics(actual: pl.Series, predicted: pl.Series) -> dict[str, float]:
    """Compute MAE, RMSE, MAPE, mean error, and std error via a single DuckDB query."""
    pl.DataFrame({"actual": actual, "predicted": predicted})
    return duckdb.sql("""
        SELECT
            AVG(POWER(actual - predicted, 2))                            AS mse,
            SQRT(AVG(POWER(actual - predicted, 2)))                      AS rmse,
            AVG(ABS(actual - predicted))                                 AS mae,
            AVG(ABS((actual - predicted) / NULLIF(actual, 0)))           AS mape,
            AVG(actual - predicted)                                      AS mean_error,
            STDDEV_SAMP(actual - predicted)                              AS std_error
        FROM df
    """).pl().row(0, named=True)


def plot_error_analysis(
    actual: pl.Series,
    predicted: pl.Series,
    title: str,
    output_path: Path,
):
    errors = (actual - predicted).to_list()

    if plot:
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

        ax1.plot(actual.to_list(),    label="Actual",    color="#4A90A4", linewidth=1.2)
        ax1.plot(predicted.to_list(), label="Predicted", color="#D4A574", linewidth=1.2)
        ax1.set_ylabel("Value")
        ax1.set_title(title)
        ax1.legend(loc="best")

        ax2.plot(errors, color="#8B6F9E", linewidth=1.2)
        ax2.axhline(0, color="k", linestyle="--", linewidth=0.8)
        ax2.set_xlabel("Time")
        ax2.set_ylabel("Error")

        plt.tight_layout()
        plt.savefig(output_path, dpi=100, bbox_inches="tight", facecolor="white")
        plt.close()

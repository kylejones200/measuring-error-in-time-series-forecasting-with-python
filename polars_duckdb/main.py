#!/usr/bin/env python3
"""Measuring forecast error — Polars + DuckDB rewrite (no sklearn.metrics)."""

import argparse
import yaml
import logging
import numpy as np
import polars as pl
from pathlib import Path

from core import calculate_error_metrics, plot_error_analysis

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def load_config(config_path: Path = None) -> dict:
    if config_path is None:
        config_path = Path(__file__).parent.parent / "config.yaml"
    with open(config_path) as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description="Forecast error — Polars + DuckDB")
    parser.add_argument("--config", type=Path, default=None)
    parser.add_argument("--data-path", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()

    config = load_config(args.config)
    output_dir = Path(args.output_dir) if args.output_dir else Path(config["output"]["figures_dir"])
    output_dir.mkdir(exist_ok=True)

    if args.data_path and args.data_path.exists():
        df = pl.read_csv(args.data_path)
        actual    = df["actual"]
        predicted = df["predicted"]
    elif config["data"]["generate_synthetic"]:
        rng = np.random.default_rng(config["data"]["seed"])
        n = config["data"]["n_periods"]
        actual_np    = np.sin(np.arange(n) / 10) + rng.normal(0, 0.10, n)
        predicted_np = actual_np + rng.normal(0, 0.15, n)
        actual    = pl.Series("actual",    actual_np.tolist())
        predicted = pl.Series("predicted", predicted_np.tolist())
    else:
        raise ValueError("No data source specified")

    metrics = calculate_error_metrics(actual, predicted)
    logging.info(f"MSE        : {metrics['mse']:.4f}")
    logging.info(f"RMSE       : {metrics['rmse']:.4f}")
    logging.info(f"MAE        : {metrics['mae']:.4f}")
    logging.info(f"MAPE       : {metrics['mape']:.2%}")
    logging.info(f"Mean error : {metrics['mean_error']:.4f}")
    logging.info(f"Std error  : {metrics['std_error']:.4f}")

    plot_error_analysis(actual, predicted, "Forecast Error Analysis",
                        output_dir / "error_analysis.png")

    logging.info(f"Analysis complete. Figures saved to {output_dir}")


if __name__ == "__main__":
    main()

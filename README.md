# Measuring Error in Time Series Forecasting with Python

This project demonstrates various error metrics for evaluating time series forecasts.

## Business context

The point of time series models is accurately forecast the future. Error measurement helps us compare models, understand where they fall short, and refine forecasting strategies.

<figcaption>Photo by <a class="markup--anchor markup--figure-anchor" rel="photo-creator noopener" target="_blank">Michael Anfang</a> on <a class="markup--anchor markup--figure-anchor"

This article introduces common error metrics used in time series forecasting, their benefits, drawbacks, and how to compute them using Python (using sklearn). This article is all about measuring errors, not about how to create forecasts.

## Article

Medium article: [Measuring Error in Time Series Forecasting with Python](https://medium.com/@kylejones_47003/measuring-error-in-time-series-forecasting-with-python-18d743a535fd)

## Project Structure

```
.
├── README.md           # This file
├── main.py            # Main entry point
├── config.yaml        # Configuration file
├── requirements.txt   # Python dependencies
├── src/               # Core functions
│   ├── core.py        # Error measurement functions
│   └── plotting.py    # Tufte-style plotting utilities
├── tests/             # Unit tests
├── data/              # Data files
└── images/            # Generated plots and figures
```

## Configuration

Edit `config.yaml` to customize:
- Data source or synthetic generation
- Output settings

## Error Metrics

### Mean Squared Error (MSE)
- Penalizes large errors more
- Sensitive to outliers

### Root Mean Squared Error (RMSE)
- Same units as the data
- Commonly used metric

### Mean Absolute Error (MAE)
- Less sensitive to outliers
- Easy to interpret

### Mean Absolute Percentage Error (MAPE)
- Scale-independent
- Useful for comparing across series

## Caveats

- By default, generates synthetic forecast data.
- MAPE can be problematic when actual values are near zero.
- Choose metrics appropriate for your use case.

## Disclaimer

Educational/demo code only. Not financial, safety, or engineering advice. Use at your own risk. Verify results independently before any production or operational use.

## License

MIT — see [LICENSE](LICENSE).
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf


def find_seasonality(data, max_lag=50):
    """
    Detect the seasonality period of a time series using autocorrelation.

    Parameters:
    - data: pandas Series or numpy array of time series data
    - max_lag: maximum number of lags to consider

    Returns:
    - seasonality_period: Number of data points in the seasonality, or None if not found
    """
    # Compute autocorrelation
    autocorr_values = acf(data, nlags=max_lag, fft=True)

    # Ignore lag 0 and find the next significant peak
    lag_indices = np.arange(1, len(autocorr_values))
    significant_peaks = np.where((autocorr_values[lag_indices] > 0.1) &
                                 (autocorr_values[lag_indices] == np.max(autocorr_values[lag_indices])))[0]

    if significant_peaks.size > 0:
        # Return the first significant peak (adjust for lag index)
        return significant_peaks[0] + 1
    return None


# Generate sample seasonal data
def generate_seasonal_data(season_length, n_points, noise_level=0.5):
    """
    Generate synthetic time series data with a given seasonality length.
    """
    time = np.arange(n_points)
    # data = 10 * np.sin(2 * np.pi * time / season_length) + np.random.normal(0, noise_level, n_points)
    data = 15  + 10 * np.sin(2 * np.pi * time / season_length) + np.random.normal(0, 2, n_points)
    return pd.Series(data)


# Main script
if __name__ == "__main__":
    # Generate a sample time series with seasonality
    season_length = 10
    seasonal_data = generate_seasonal_data(season_length=season_length, n_points=500)

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(seasonal_data, label="Time Series")
    plt.title("Time Series Data with Seasonality")
    plt.legend()
    plt.show()

    # Find seasonality period
    detected_seasonality = find_seasonality(seasonal_data, max_lag=30)
    if detected_seasonality:
        print(f"Detected seasonality period: {detected_seasonality} data points (True: {season_length})")
    else:
        print("No seasonality detected within the given range of lags.")

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


def plot_metrics(csv_file):
    """
    Reads a .csv file containing metrics and their values, and plots the data.

    Args:
        csv_file (str): Path to the .csv file. The file should have two columns: 'Metric' and 'Value'.
    """
    try:
        # Read the CSV file
        data = pd.read_csv(csv_file)

        # Check if the necessary columns exist
        if 'timestamp' not in data.columns or 'value' not in data.columns:
            raise ValueError("The .csv file must contain 'Metric' and 'Value' columns.")

        print(f"Shape of DataFrame: {data.shape}")     # Tuple of (rows, columns)
        print(f"len of DataFrame: {len(data)}")  # Tuple of (rows, columns)

        # Extract metrics and values
        # metrics = data['timestamp'][:1000]
        metrics = np.arange(1, len(data) + 1)
        values = data['value'][:len(data)]


        # Plot the data
        plt.figure(figsize=(50, 10))
        plt.plot(metrics, values, color='green')
        plt.xlabel('Metrics')
        plt.ylabel('Values')
        plt.title('Metrics vs. Values')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Show the plot
        plt.show()

    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
csv_file_path = "data/realKnownCause/ec2_request_latency_system_failure.csv"  # Replace with your actual file path
plot_metrics(csv_file_path)

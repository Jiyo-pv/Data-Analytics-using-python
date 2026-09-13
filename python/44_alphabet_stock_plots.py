"""Question 44: Plot Alphabet stock data between two dates.

Usage: python 44_alphabet_stock_plots.py [csv_path] [start_date] [end_date]
"""

import argparse

import matplotlib.pyplot as plt
import pandas as pd


def load_stock_data(path, start_date, end_date):
    data = pd.read_csv(path)
    data.columns = [column.strip() for column in data.columns]
    date_column = next(column for column in data.columns if column.lower() in {"date", "datetime"})
    data[date_column] = pd.to_datetime(data[date_column])
    selected = data[data[date_column].between(start_date, end_date)].copy()
    selected.sort_values(date_column, inplace=True)
    return selected, date_column


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", nargs="?", default="alphabet_stock_data.csv")
    parser.add_argument("start_date", nargs="?", default="2024-01-01")
    parser.add_argument("end_date", nargs="?", default="2024-12-31")
    args = parser.parse_args()

    data, date_column = load_stock_data(args.csv_path, args.start_date, args.end_date)
    required = {"Open", "Close", "High", "Low", "Volume"}
    missing = required.difference(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    figure, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes[0, 0].plot(data[date_column], data["Close"])
    axes[0, 0].set_title("Closing price")
    axes[0, 1].bar(data[date_column], data["Volume"])
    axes[0, 1].set_title("Trading volume")
    axes[1, 0].hist(data[["Open", "Close", "High", "Low"]], bins=30, stacked=True, label=["Open", "Close", "High", "Low"])
    axes[1, 0].set_title("Price distribution")
    axes[1, 0].legend()
    axes[1, 1].scatter(data["Volume"], data["Close"], alpha=0.6)
    axes[1, 1].set_title("Volume vs closing price")
    axes[1, 1].set_xlabel("Volume")
    axes[1, 1].set_ylabel("Close")
    figure.autofmt_xdate()
    figure.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

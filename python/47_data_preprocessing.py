"""Question 47: Clean, encode, scale, and visualize a CSV dataset.

Usage: python 47_data_preprocessing.py [csv_path]
"""

import argparse

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler


def preprocess_data(path):
    data = pd.read_csv(path)
    numeric_columns = data.select_dtypes(include="number").columns
    categorical_columns = data.select_dtypes(exclude="number").columns

    for column in numeric_columns:
        data[column] = data[column].fillna(data[column].median())
    for column in categorical_columns:
        mode = data[column].mode()
        if not mode.empty:
            data[column] = data[column].fillna(mode.iloc[0])

    encoded = pd.get_dummies(data, columns=list(categorical_columns), dtype=float)
    scaled = encoded.copy()
    if len(numeric_columns) > 0:
        scaler = StandardScaler()
        scaled[list(numeric_columns)] = scaler.fit_transform(scaled[list(numeric_columns)])
    return data, encoded, scaled


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", nargs="?", default="Data.csv")
    args = parser.parse_args()

    cleaned, encoded, scaled = preprocess_data(args.csv_path)
    print("Cleaned data:")
    print(cleaned)
    print("Encoded and scaled data:")
    print(scaled)

    numeric_columns = cleaned.select_dtypes(include="number").columns
    if len(numeric_columns) > 0:
        cleaned[numeric_columns].hist(figsize=(10, 6))
        plt.suptitle("Numeric feature distributions")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()

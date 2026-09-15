"""Simple version of Qn 47: clean missing values, encode categories, scale features, and plot."""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler


def preprocess_data(path):
    data = pd.read_csv(path)

    numeric_cols = data.select_dtypes(include="number").columns
    categorical_cols = data.select_dtypes(exclude="number").columns

    for col in numeric_cols:
        data[col] = data[col].fillna(data[col].median())

    for col in categorical_cols:
        if data[col].mode().size > 0:
            data[col] = data[col].fillna(data[col].mode()[0])

    encoded = pd.get_dummies(data, columns=list(categorical_cols), dtype=float)

    scaled = encoded.copy()
    if len(numeric_cols) > 0:
        scaler = StandardScaler()
        scaled[list(numeric_cols)] = scaler.fit_transform(encoded[list(numeric_cols)])

    return data, encoded, scaled


if __name__ == "__main__":
    cleaned, encoded, scaled = preprocess_data("Data.csv")

    print("Cleaned data:")
    print(cleaned)
    print("\nEncoded data:")
    print(encoded)
    print("\nScaled data:")
    print(scaled)

    scaled[numeric_cols := cleaned.select_dtypes(include="number").columns].hist(figsize=(10, 6))
    plt.suptitle("Numeric feature distribution after preprocessing")
    plt.tight_layout()
    plt.show()

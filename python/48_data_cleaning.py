import pandas as pd

# Read the CSV file
data = pd.read_csv("dirtydata.csv")

# 1. Handle empty cells
print("Rows after dropna():", len(data.dropna()))

# 2. Replace empty Calories with mean
data["Calories"] = data["Calories"].fillna(
    data["Calories"].mean()
)

# 3. Replace empty Duration with median
data["Duration"] = data["Duration"].fillna(
    data["Duration"].median()
)

# 4. Replace empty Date with mode
data["Date"] = data["Date"].fillna(
    data["Date"].mode()[0]
)

# 5. Handle wrong Date format
data["Date"] = pd.to_datetime(
    data["Date"],
    format="mixed"
)

# 6. Handle wrong Duration data
# Replace 450 with mean Duration
data["Duration"] = data["Duration"].replace(
    450,
    int(data["Duration"].mean())
)

# 7. Remove duplicates
data = data.drop_duplicates()

# Final cleaned data
print("\nFinal cleaned data:")
print(data)
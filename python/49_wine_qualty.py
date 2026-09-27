import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


# ---------------------------------------------------
# 1. Load the datasets
# ---------------------------------------------------

red = pd.read_csv("winequality-red.csv", sep=";")
white = pd.read_csv("winequality-white.csv", sep=";")

print("Red Wine Shape:", red.shape)
print("White Wine Shape:", white.shape)

print("\nRed Wine Columns:")
print(red.columns)

print("\nWhite Wine Columns:")
print(white.columns)

print("\nFirst 5 Red Wine Rows:")
print(red.head())

print("\nFirst 5 White Wine Rows:")
print(white.head())


# ---------------------------------------------------
# 2. Add wine_type column
# ---------------------------------------------------

red["wine_type"] = "red"
white["wine_type"] = "White"


# ---------------------------------------------------
# 3. Check whether columns are identical
# ---------------------------------------------------

print("\nAre columns identical?")
print(red.columns[:-1].equals(white.columns[:-1]))


# ---------------------------------------------------
# 4. Combine both datasets
# ---------------------------------------------------

data = pd.concat([red, white], ignore_index=True)

print("\nIntegrated Dataset Shape:")
print(data.shape)

print("\nUnique wine types:")
print(data["wine_type"].unique())


# ---------------------------------------------------
# 5. Save integrated dataset
# ---------------------------------------------------

data.to_csv("integrated_wine_quality.csv", index=False)

print("\nIntegrated dataset saved.")


# ---------------------------------------------------
# 6. Check missing values
# ---------------------------------------------------

print("\nMissing Values:")
print(data.isnull().sum())


# ---------------------------------------------------
# 7. Check and remove duplicates
# ---------------------------------------------------

print("\nNumber of duplicate rows:")
print(data.duplicated().sum())

data = data.drop_duplicates()

print("Shape after removing duplicates:")
print(data.shape)


# ---------------------------------------------------
# 8. Define X and y
# ---------------------------------------------------

X = data.drop("quality", axis=1)
y = data["quality"]


# ---------------------------------------------------
# 9. Encode wine_type
# ---------------------------------------------------

X = pd.get_dummies(X, columns=["wine_type"], drop_first=True)

print("\nFeatures after encoding:")
print(X.columns)


# ---------------------------------------------------
# 10. Split into training and testing data
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining rows:", len(X_train))
print("Testing rows:", len(X_test))


# ---------------------------------------------------
# 11. Feature Scaling
# ---------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# ---------------------------------------------------
# 12. Distribution of quality scores
# ---------------------------------------------------

plt.figure(figsize=(8, 5))
sns.histplot(data["quality"], bins=10, kde=True)
plt.title("Distribution of Wine Quality")
plt.xlabel("Quality")
plt.ylabel("Count")
plt.show()


# ---------------------------------------------------
# 13. Distribution of quality by wine type
# ---------------------------------------------------

plt.figure(figsize=(8, 5))
sns.boxplot(x="wine_type", y="quality", data=data)
plt.title("Quality Distribution by Wine Type")
plt.show()


# ---------------------------------------------------
# 14. Average quality of red and white wine
# ---------------------------------------------------

print("\nAverage Quality:")
print(data.groupby("wine_type")["quality"].mean())


# ---------------------------------------------------
# 15. Correlation heatmap
# ---------------------------------------------------

correlation = data.select_dtypes(include="number").corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# ---------------------------------------------------
# 16. Top 3 features correlated with quality
# ---------------------------------------------------

quality_corr = correlation["quality"].drop("quality")

top_3 = quality_corr.abs().sort_values(
    ascending=False
).head(3)

print("\nTop 3 Features Correlated with Quality:")
print(top_3)


# ---------------------------------------------------
# 17. Alcohol vs Quality
# ---------------------------------------------------

plt.figure(figsize=(8, 5))
sns.scatterplot(
    x="alcohol",
    y="quality",
    hue="wine_type",
    data=data
)

plt.title("Alcohol vs Quality")
plt.xlabel("Alcohol")
plt.ylabel("Quality")
plt.show()


# ---------------------------------------------------
# 18. Linear Regression
# ---------------------------------------------------

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

linear_prediction = linear_model.predict(X_test)


# ---------------------------------------------------
# 19. Decision Tree Regression
# ---------------------------------------------------

tree_model = DecisionTreeRegressor(
    random_state=42
)

tree_model.fit(X_train, y_train)

tree_prediction = tree_model.predict(X_test)


# ---------------------------------------------------
# 20. Random Forest Regression
# ---------------------------------------------------

forest_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

forest_model.fit(X_train, y_train)

forest_prediction = forest_model.predict(X_test)


# ---------------------------------------------------
# 21. Model Evaluation
# ---------------------------------------------------

def evaluate_model(name, actual, prediction):

    r2 = r2_score(actual, prediction)
    mae = mean_absolute_error(actual, prediction)
    mse = mean_squared_error(actual, prediction)
    rmse = mse ** 0.5

    print("\n", name)
    print("R2 Score:", r2)
    print("MAE:", mae)
    print("MSE:", mse)
    print("RMSE:", rmse)


evaluate_model(
    "Linear Regression",
    y_test,
    linear_prediction
)

evaluate_model(
    "Decision Tree Regressor",
    y_test,
    tree_prediction
)

evaluate_model(
    "Random Forest Regressor",
    y_test,
    forest_prediction
)
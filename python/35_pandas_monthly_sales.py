"""Question 35: Find peak monthly sales and plot product sales."""

import matplotlib.pyplot as plt
import pandas as pd


sales = pd.DataFrame(
    {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Product A": [120, 135, 150, 145, 170, 180],
        "Product B": [100, 110, 125, 130, 140, 155],
        "Product C": [90, 95, 105, 115, 120, 135],
    }
)

product_columns = ["Product A", "Product B", "Product C"]
sales["Total"] = sales[product_columns].sum(axis=1)
peak_month = sales.loc[sales["Total"].idxmax(), "Month"]
print(sales)
print("Month with highest total sales:", peak_month)

sales.plot(x="Month", y=product_columns, kind="bar", figsize=(8, 5))
plt.title("Monthly Product Sales")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

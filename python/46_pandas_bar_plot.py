"""Question 46: Create a grouped bar plot from a DataFrame."""

import matplotlib.pyplot as plt
import pandas as pd


data = pd.DataFrame(
    {
        "a": [2, 4, 6, 8, 10],
        "b": [4, 2, 4, 2, 2],
        "c": [8, 3, 7, 6, 4],
        "d": [5, 4, 4, 4, 3],
        "e": [7, 2, 7, 8, 3],
    }
)

data.plot(x="a", y=["b", "c", "d", "e"], kind="bar", figsize=(9, 5))
plt.xlabel("a")
plt.ylabel("Values")
plt.title("Grouped bar plot")
plt.tight_layout()
plt.show()

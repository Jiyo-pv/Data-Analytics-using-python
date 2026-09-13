"""Question 45: Create multiple plots in one figure."""

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1, 7)
values = np.array([12, 18, 15, 22, 20, 26])

figure, axes = plt.subplots(2, 2, figsize=(10, 7))
axes[0, 0].plot(x, values, marker="o")
axes[0, 0].set_title("Line plot")
axes[0, 1].bar(x, values)
axes[0, 1].set_title("Bar plot")
axes[1, 0].scatter(x, values)
axes[1, 0].set_title("Scatter plot")
axes[1, 1].pie(values, labels=[f"Item {value}" for value in x], autopct="%1.0f%%")
axes[1, 1].set_title("Pie chart")
figure.tight_layout()
plt.show()

"""Question 36: Analyze and plot seven days of weather data."""

import matplotlib.pyplot as plt
import pandas as pd


weather = pd.DataFrame(
    {
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Temperature": [29, 31, 30, 28, 27, 26, 29],
        "Humidity": [65, 60, 72, 75, 70, 68, 63],
        "Rainfall": [0, 2, 5, 12, 8, 1, 0],
    }
)

print(weather)
print("Average temperature:", weather["Temperature"].mean())
print("Total rainfall:", weather["Rainfall"].sum())

weather.plot(x="Day", y="Temperature", marker="o", figsize=(8, 5))
plt.title("Temperature by Day")
plt.ylabel("Temperature (C)")
plt.tight_layout()
plt.show()

"""Question 43: Group a DataFrame by all columns and count each group."""

import pandas as pd


data = pd.DataFrame(
    {
        "Id": [1, 2, 1, 1, 2, 1, 2],
        "type": [10, 15, 11, 20, 21, 12, 14],
        "book": ["Math", "English", "Physics", "Math", "English", "Physics", "English"],
    }
)

groups = data.groupby(list(data.columns), dropna=False).size().rename("count")
print(groups.reset_index())

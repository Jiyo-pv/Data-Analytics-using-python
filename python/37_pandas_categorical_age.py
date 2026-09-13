"""Question 37: Convert continuous age values into categories."""

import pandas as pd


people = pd.DataFrame(
    {
        "Name": ["Alberto Franco", "Gino Mcneill", "Ryan Parkes", "Eesha Hinton", "Syed Wharton"],
        "Age": [18, 22, 40, 50, 80],
    }
)

people["AgeCategory"] = pd.cut(
    people["Age"],
    bins=[0, 18, 35, 60, float("inf")],
    labels=["Teen", "Young adult", "Adult", "Senior"],
    include_lowest=True,
)

print(people)

"""Question 33: Build and filter a student DataFrame from Series."""

import pandas as pd


name = pd.Series(["Asha", "Ben", "Chitra", "Dev", "Esha"], name="Name")
age = pd.Series([19, 20, 21, 19, 22], name="Age")
course = pd.Series(["Python", "SQL", "Python", "Statistics", "Python"], name="Course")
marks = pd.Series([78, 35, 91, 42, 28], name="Marks")

students = pd.concat([name, age, course, marks], axis=1)
students["Result"] = students["Marks"].ge(40).map({True: "Pass", False: "Fail"})

print(students)
print("Passed students:")
print(students[students["Result"] == "Pass"])

"""Question 34: Analyze employee salaries by department."""

import pandas as pd


employees = pd.DataFrame(
    {
        "EmployeeID": [101, 102, 103, 104, 105],
        "Name": ["Asha", "Ben", "Chitra", "Dev", "Esha"],
        "Department": ["IT", "HR", "IT", "Sales", "HR"],
        "Salary": [72000, 58000, 91000, 64000, 61000],
    }
)

print(employees)
print("Average salary by department:")
print(employees.groupby("Department")["Salary"].mean())
print("Highest-paid employee:")
print(employees.loc[employees["Salary"].idxmax()])

"""Question 40: Append student data and merge it with exam data."""

import pandas as pd


students = pd.DataFrame(
    {
        "student_id": ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"],
        "name": ["Danniella Fenton", "Ryder Storey", "Bryce Jensen", "Ed Bernal", "Kwame Morin", "Dante Morse", "Kaiser William", "Madeeha Preston"],
        "marks": [200, 210, 190, 222, 199, 198, 219, 201],
    }
)
exam_data = pd.DataFrame(
    {
        "student_id": ["S1", "S2", "S3", "S4", "S5", "S7", "S8", "S9", "S10", "S11", "S12", "S13"],
        "exam_id": [23, 45, 12, 67, 21, 55, 33, 14, 56, 83, 88, 12],
    }
)

print(students.merge(exam_data, on="student_id", how="left"))

"""Question 31: NumPy array creation, reshaping, aggregation, and filtering."""

import numpy as np


numbers = np.arange(1, 21)
matrix = numbers.reshape(4, 5)

print("1D array:")
print(numbers)
print("4x5 matrix:")
print(matrix)
print("Transpose:")
print(matrix.T)
print("Total sum:", matrix.sum())
print("Row sums:", matrix.sum(axis=1))
print("Column sums:", matrix.sum(axis=0))
print("Even numbers:", numbers[numbers % 2 == 0])

"""Question 32: NumPy slicing operations on a 5x5 array."""

import numpy as np


array = np.arange(1, 26).reshape(5, 5)
center = array[1:4, 1:4]

print("Array:")
print(array)
print("Center 3x3:")
print(center)
print("Reversed center 3x3:")
print(center[::-1, ::-1])
print("First 2 rows and last 2 columns:")
print(array[:2, -2:])
print("All elements in one line:")
print(array.ravel())

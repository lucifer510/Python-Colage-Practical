# Write a NumPy program to find common values between two arrays.

import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([4, 5, 6, 7, 8, 9])
print(np.intersect1d(x, y)) # prints "[4 5 6]"

# Write a NumPy program to Generate matrix using random integers between 10 and 30.

import numpy as np

matrix = np.random.randint(10, 30, (3, 3))
print(matrix)  # Prints "[[28 29 11]
#                        [14 23 10]
#                        [12 28 23]]"

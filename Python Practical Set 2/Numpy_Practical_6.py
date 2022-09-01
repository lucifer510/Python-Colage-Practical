# Write a NumPy program to Shuffle numbers between 0 and 10.

import numpy as np

x = np.random.randint(0, 10, 10)
print(f"Original Array: \n{x}")  # Prints "Original Array:
#                                          [3 7 0 1 4 2 6 0 3 1]"
np.random.shuffle(x)
print(f"Shuffled Array: \n{x}")  # Prints "Shuffled Array:
#                                          [0 6 1 3 1 4 3 2 7 0]"

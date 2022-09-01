# Write a NumPy program to round elements of the array to the nearest integer.
import numpy as np

x = np.array([-.7, -1.5, -1.7, 0.3, 1.5, 1.8, 2.0])
print(f"Original array: {x}")  # Prints "Original array: [-0.7 -1.5 -1.7  0.3  1.5  1.8  2. ]"
x = np.rint(x)
print(f"Round elements of the array to the nearest integer: {x}")  # Prints "Original array: [-0.7 -1.5 -1.7  0.3  1.5  1.8  2. ]"

# Write a NumPy program to create a null vector of size 10 and update the sixth value to
# 11.
import numpy as np

zero = np.zeros(10, dtype=np.int64)  # Create a null vector of size 10.
zero[6] = 11  # Update the Sixth value to 11.
print(zero)  # Prints "[ 0  0  0  0  0  0 11  0  0  0]"



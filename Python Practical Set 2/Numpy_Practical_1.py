# Write a NumPy program to create an element-wise comparison (greater, greater_equal,
# less, and less_equal) of two given arrays.

import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 4, 5, 6, 7])

print("Greater than or equal to: " , np.greater_equal(x, y))  # Prints "Greater than or equal to:  [False False False False False]"
print("Greater than: ",np.greater(x, y))  # Prints "Greater than:  [False False False False False]"
print("Less than or equal to: " , np.less_equal(x, y))  # Prints "Less than or equal to:  [ True  True  True  True  True]"
print("Less than: " , np.less_equal(x, y))  # Prints "Less than:  [ True  True  True  True  True]"

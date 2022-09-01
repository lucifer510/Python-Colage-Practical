# Write a NumPy program to perform row wise and column wise sorting of given array.

import numpy as np

arr = np.random.randint(10, 30, (3, 3))
print("Original Array: \n", arr)
arr1 = np.sort(arr, axis=1)
print("Row Wise Array: \n", arr1)
arr2 = np.sort(arr, axis=0)
print("Column Wise Array: \n", arr2)

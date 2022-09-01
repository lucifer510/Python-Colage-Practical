# Write a NumPy program to find Row Wise and column wise maximum from two matrix

import numpy as np

arr = np.random.randint(1, 30, (3, 3))
print("Original matrix: \n", arr)
RowWiseMax = np.max(arr, axis=1)
print("Row Wise Max Element: ", RowWiseMax)
ColumnWiseMax = np.max(arr, axis=0)
print("Column Wise Max Element: ", ColumnWiseMax)

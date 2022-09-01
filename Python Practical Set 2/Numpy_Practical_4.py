# Write a NumPy program to create a new shape to an array without changing its data.

import numpy as np

array = np.random.randint(10, 20, (3, 2), int)
print(f"Creating a new shape Array...\n{array}")  # May Be Prints "Creating a new shape Array...
#                                                                  [[18 14]
#                                                                   [19 11]
#                                                                   [13 16]]"
print(f"Creating a new shape Array without  changing its data...\n{np.reshape(array, (2, 3))}")  # May Be Prints "Creating a new shape Array without changing its data...
#                                                                                                                 [[18 14 19]
#                                                                                                                  [11 13 16]] "

# Write a NumPy program to count the number of days and number of weekdays in August
# 2022.

import numpy as np

days = np.datetime64('2022-09-01') - np.datetime64('2022-08-01')
print(f"Total Number of days in August 2022: {days}")  # Prints "Total Number of days in August 2022: 31 days"
weekdays = np.busday_count('2022-08-01', '2022-09-01')
print(f"Total Number of weekdays in August 2022: {weekdays}")  # Prints "Total Number of weekdays in August 2022: 23"

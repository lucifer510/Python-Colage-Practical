# Write a Pandas program to Sort the diamonds data based on length ascending and
# descending both.

import pandas as pd

data = pd.read_csv(r"C:\Users\MIHIR\Desktop\Sem 5\PDS\CO3 Material\diamonds.csv")
print(data.head(3))
ascending = data.sort_values(by='x', ascending=True)
print(ascending.head(3))
decending = data.sort_values(by='x', ascending=False)
print(decending.head(3))

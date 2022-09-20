# Write a Pandas program to find the details of the diamonds where depth>61, price>340,
# and cut=’Good’.

import pandas as pd

data = pd.read_csv(r"C:\Users\MIHIR\Desktop\Sem 5\PDS\CO3 Material\diamonds.csv")

# Original data frame
print("Original data frame:")
print(data.head(3))

# Updated data frame
print("Updated data frame:")
data = data[(data.depth > 61) & (data.price > 340) & (data.cut == 'Good')]
print(data.head(3))

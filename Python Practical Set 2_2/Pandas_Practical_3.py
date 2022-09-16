# Write a Pandas program to select a series from diamonds Data Frame. Print the content
# of the series.

import pandas as pd

data = pd.read_csv(r"C:\Users\MIHIR\Desktop\Sem 5\PDS\CO3 Material\diamonds.csv")
print(data['price'])
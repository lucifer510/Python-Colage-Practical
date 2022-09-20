# Write a Pandas program to remove the second column of the diamonds Data frame.

import pandas as pd

data = pd.read_csv(r"C:\Users\MIHIR\Desktop\Sem 5\PDS\CO3 Material\diamonds.csv")
print(data.head())
data.drop('cut', axis=1, inplace=True)
print(data.head())

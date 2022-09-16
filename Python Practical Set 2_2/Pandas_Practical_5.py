# Write a Pandas program to rename two of the columns of the diamonds Data frame.

import pandas as pd

data = pd.read_csv(r"C:\Users\MIHIR\Desktop\Sem 5\PDS\CO3 Material\diamonds.csv")
print(data.head(4))
data.rename(columns={'color': 'diamond_color', 'clarity': 'dimaond_clarity'}, inplace=True)
print(data.head(4))


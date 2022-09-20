# Write a Pandas program to calculate the count, the minimum, and maximum price for
# each cut of diamonds Data Frame.
import pandas as pd

data = pd.read_csv(r"C:\Users\MIHIR\Desktop\Sem 5\PDS\CO3 Material\diamonds.csv")

print("Original Dataframe:")
print(data.head(3))
print("\nCount, minimum, maximum  price for each cut of diamonds DataFrame:")
print(data.groupby('cut').price.agg(['count', 'min', 'max']))
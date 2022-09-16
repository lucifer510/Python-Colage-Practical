# Write a Pandas program to read a CSV file from a specified source and print the first 10
# rows.
import pandas as pd

data = pd.read_csv(r"C:\Users\MIHIR\Desktop\Sem 5\PDS\CO3 Material\diamonds.csv")
print(data.head(10))

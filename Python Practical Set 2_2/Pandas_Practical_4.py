# Write a Pandas program to find the number of rows and columns and the data type of
# each column of the diamonds Data frame.
import pandas as pd

data = pd.read_csv(r"C:\Users\MIHIR\Desktop\Sem 5\PDS\CO3 Material\diamonds.csv")
print(data.shape)
print(data.dtypes)

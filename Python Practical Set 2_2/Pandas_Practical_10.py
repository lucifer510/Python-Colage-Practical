# Write Pandas program to Demonstrate handling of Missing values (Remove column,
# Remove rows and Filling values Etc.)

import pandas as pd

data = pd.read_csv(r"C:\Users\MIHIR\Desktop\Sem 5\PDS\CO3 Material\diamonds.csv")

# Describe Basic Information
print(data.info())
print(data.isnull().sum())
print(data.describe())

# print Null values row
print(data[data['table'].isna()])

# Remove rows or column
updated_data=data.dropna(axis=1)
print(updated_data)
print(updated_data.info())

# Fill missing values
updated_data = data
print(updated_data.info())

updated_data['table']=updated_data['table'].fillna(updated_data['table'].mean())
# Display after update
print(updated_data.info())
print(updated_data[7:87])
print(updated_data[updated_data['table'].isna()])
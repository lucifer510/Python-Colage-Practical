# Write a program to demonstrate the Groupby, Join and Merge.
import pandas as pd

a = pd.DataFrame({'column1': ['A', 'C', 'D', 'E'],
                  'column2': ['F', 'G', 'H', 'I'],
                  'column3': ['J', 'K', 'L', 'M'],
                  'column4': ['N', 'O', 'P', 'Q']},
                 index=[1, 2, 3, 4])
b = pd.DataFrame({'column3': ['R', 'S', 'T', 'U'],
                  'column5': ['V', 'W', 'X', 'Y'],
                  'column6': ['Z', 'α', 'β', 'υ'],
                  'column7': ['σ', 'χ', 'ι', 'κ']},
                 index=[3, 4, 5, 6])
result = pd.concat([a, b], axis=0, join='outer')  # outer join with axis 0
print(result)
result = pd.concat([a, b], axis=1, join='outer')  # outer join with  axis=1
print(result)
result = pd.concat([a, b], axis=0, join='inner')  # inner join with axis 0
print(result)
result = pd.concat([a, b], axis=1, join='inner')  # inner join with  axis=1
print(result)

# Demonstrate Merge
c = pd.DataFrame({'key': ['A', 'C', 'D', 'E'],
                  'column2': ['F', 'G', 'H', 'I'],
                  'column3': ['J', 'K', 'L', 'M'],
                  'column4': ['N', 'O', 'P', 'Q']},
                 index=[1, 2, 3, 4])
d = pd.DataFrame({'key': ['C', 'D', 'T', 'U'],
                  'column5': ['V', 'W', 'X', 'Y'],
                  'column6': ['Z', 'α', 'β', 'υ'],
                  'column7': ['σ', 'χ', 'ι', 'κ']},
                 index=[3, 4, 5, 6])
result = pd.merge(c, d, on='key')
print(result)

# Demonstrate Groupby

e = pd.DataFrame({"key": ["a", "b", "c", "a", "b", "c"], "values": [1, 2, 3, 1, 2, 3]})
f = e.groupby("key").sum()
print(f)

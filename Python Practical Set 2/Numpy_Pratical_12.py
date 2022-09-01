# Write a NumPy program to capitalize the first letter, lowercase, uppercase, swapcase,
# title-case of all the elements of a given array.
import numpy as np

arr = np.array(['mIHIR', 'MIHIR', 'mihir', 'MiHiR'], dtype=np.str_)
print("Original Array:")
print(arr)
capitalized_case = np.char.capitalize(arr)
lowered_case = np.char.lower(arr)
uppered_case = np.char.upper(arr)
swapcased_case = np.char.swapcase(arr)
titlecased_case = np.char.title(arr)
print("\nCapitalized: ", capitalized_case)
print("Lowered: ", lowered_case)
print("Uppered: ", uppered_case)
print("Swapcased: ", swapcased_case)
print("Titlecased: ", titlecased_case)

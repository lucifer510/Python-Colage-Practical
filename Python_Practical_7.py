# Python Program to Split the array and add the first part to the end of second part.
arr = [55, 66, 42, 31, 98, 52, 67, 12]
splitPart = int(input(f"Enter Index Of Array (0 to {len(arr)}) From Where You Want to Split it : \n"))

firstPart = arr[0:splitPart]
secondPart = arr[splitPart:]

newArray = secondPart + firstPart
print(f"Resulted Array Is : {newArray}")

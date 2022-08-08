# Python Program for rotate the elements of array.
ar = [1, 2, 3, 4, 5]

print(f"array before rotation : {ar}")


def rotateArray(ar, d=1):
    ar[:] = ar[d:len(ar)] + ar[0:d]
    return ar


d = int(input("Enter How Many Times Do You Want To Rotate Array: "))
print(f"Array After {d} Left Rotation : {rotateArray(ar, d)}")

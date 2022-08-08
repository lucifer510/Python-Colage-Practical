# Python program to print even numbers and duplicate from a list

# For Duplicate Numbers
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


list1 = [12, 10, 20, 30, 15, 20, 24, 12, 65, 76, 15]

# For Even Number
print("Even Numbers From The List Is : ")
for num in list1:

    # checking condition
    if num % 2 == 0:
        print(num, end=" ")
print(f"\nRepeated Numbers From the List Is : {Repeat(list1)}")

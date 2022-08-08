# Python Program to check if given array is Monotonic or not.

n = int(input("Enter How Many Elements Do You Want to Enter In Array: \n"))
arr = []
print("Enter Elements: \n")
for i in range(n):
    arr.append(int(input()))


def isMonotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))


print(isMonotonic(arr))

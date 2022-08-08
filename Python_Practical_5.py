# Write a Python program to print all Prime numbers in an Interval using user defined
# function
lb = int(input("Enter Lower Bound Value: "))
ub = int(input("Enter Upper Bound Value: "))


def primeNum(lb, ub):
    for num in range(lb, ub + 1):

        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


primeNum(lb, ub)

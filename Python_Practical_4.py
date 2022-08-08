# Write a Python program to check if the number provided by the user is an Armstrong
# number. Perform it with and without user defined function.

def armstrongNumber(num):
    num0 = num

    sum = 0
    while (num != 0):
        digit = num % 10
        num2 = num // 10
        num = num2
        sum = digit ** 3 + sum
    if sum == num0:
        print(f"{num0} is a armstrong number")
    else:
        print(f"{num0} is not an armstrong number")


num = int(input("Please Enter The Number: \n"))
armstrongNumber(num)

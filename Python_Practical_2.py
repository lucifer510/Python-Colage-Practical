# Fibonacci Series
n = int(input("Enter How Many Elements You Want In Series: "))

n1 = 0
n2 = 1
count = 0
if n == 1:
    print(n1)
else:
    while count < n:
        print(n1, end=",")
        nth = n2 + n1
        n1, n2 = n2, nth
        count += 1

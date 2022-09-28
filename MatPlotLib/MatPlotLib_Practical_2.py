# Write a python program to draw a line graph X = [1,2,3,4] and Y = x^2 mention label as "Value(X)" and "Square(Y)".

from matplotlib import pyplot as plt

x = [1, 2, 3, 4]
y = [x ** 2 for x in x]

plt.plot(x, y, marker='o', label='x^2')
plt.xlabel('Value(X)')
plt.ylabel('Square(Y)')

plt.legend()

plt.show()

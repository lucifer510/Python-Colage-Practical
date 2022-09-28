# Write a Python program to create pie chart of House construction cost. (Labour cost 33%,
# Plumbing 12%, Bricks 10%, Cement 20%, Steel 25%)

from matplotlib import pyplot as plt

labels = 'Labour cost', 'Plumbing', 'Bricks', 'Cement', 'Steel'
sizes = [33, 12, 10, 20, 25]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.show()

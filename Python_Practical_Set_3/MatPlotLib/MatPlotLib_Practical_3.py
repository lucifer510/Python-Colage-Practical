# Write a Python programming to display a bar chart of the popularity of programming
# Languages.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

from matplotlib import pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.bar(languages, popularity, width=0.5, color=['red', 'blue', 'green', 'yellow', 'orange', 'purple'])

plt.xlabel('Programming Languages')
plt.ylabel('Popularity')

plt.show()

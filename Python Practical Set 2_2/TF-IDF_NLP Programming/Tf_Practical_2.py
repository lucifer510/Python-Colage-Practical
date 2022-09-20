# Write a program to read an HTML file using the beautiful soup library and parse the
# following information.
# a. To read all the hyperlinks
# b. To real head part
# c. To real table data
# d. After reading all the information shown in a proper format

import requests
from bs4 import BeautifulSoup

html = requests.get("http://www.python.org").text
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')
head = soup.find_all('head')
table = soup.find_all('table')
for i in links:
    print(i.get('href'))
for i in head:
    print(i)
for i in table:
    print(i)

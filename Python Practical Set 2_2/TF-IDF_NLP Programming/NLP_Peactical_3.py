# Write NLP program using NLTK library to read text data from website and convert
# into appropriate feature table using Bag of words method.

import nltk
import pandas as pd
import requests
from bs4 import BeautifulSoup

html = requests.get("http://www.python.org").text
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()

# Tokenization
tokens = [t for t in text.split()]
print(tokens)

# Frequency distribution
freq = nltk.FreqDist(tokens)
for key, val in freq.items():
    print(str(key) + ':' + str(val))

# Frequency distribution plot
freq.plot(20, cumulative=False)


# Bag of words
def bag_of_words(words):
    return dict([(word, True) for word in words])


# Get features
words = bag_of_words(tokens)
print(words)

# Data frame
df = pd.DataFrame(words.items(), columns=['words', 'count'])
print(df)

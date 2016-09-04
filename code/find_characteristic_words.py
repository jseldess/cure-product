# Find words that characterize a text. 
# len(w) > ensures that the words are longer than the specified number of letters
# fdist1[w] > ensures that these words occur more than the specified number of times
# Page 19 of Natrual Language Processing with Python

import nltk
from nltk import FreqDist

f = open("source.txt").read().decode('utf-8')
tokens = nltk.word_tokenize(f)
text = nltk.Text(tokens)
fdist1 = FreqDist(text)
print [w for w in set(text) if len(w) > 7  and fdist1[w] > 80 and w.isalpha()]

import os
import pandas as pd
import csv
import nltk

import random
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
#from tkinter import *

#NLP Analysis of columbus's jurnal
columbus_pos = open("columbus.txt", "r").read()

#print(columbus_pos)

documents = []
removelist = ["''"]


for r in columbus_pos.split('\n'):
    documents.append((r, "pos"))

stop_words = stopwords.words('english')
#print(stop_words)
#print(len(columbus_pos))
#print(documents)

# Slice text in words
#print(nltk.word_tokenize(columbus_pos))

wtokens = nltk.word_tokenize(columbus_pos)
#print(len(wtokens) )    # Number of words in text

table = str.maketrans('', '', string.punctuation)
removed = [w.translate(table) for w in wtokens]
print("Removed : ", removed) # show what is removed

stop_words = set(stopwords.words('english'))
words = [w for w in removed if not w in stop_words]
#print(words)

#print(nltk.FreqDist(words))

wordfreq = [w for w in nltk.FreqDist(removed)]
#for w in wordfreq:
    #print(w, len(w), nltk.FreqDist(w))

# Calculate frequency distribution
fdist = nltk.FreqDist(words)

for w, frequency in fdist.most_common(20000):
    print(w, len(w), frequency)

with open('wordfrequency.csv','w') as csvfile:
    fieldnames=['word','length', 'frequency']
    writer=csv.writer(csvfile)
    writer.writerow(fieldnames)
    for w, frequency in fdist.most_common(2000):
        print(w, len(w), frequency)

        writer.writerow([w] + [len(w)] + [frequency])


wfreq = nltk.FreqDist(wtokens)

#print(wfreq)

print("Number of unique words in text : ", len(wfreq))  # Number of unique words in text

#print(wfreq.most_common(40) )    # 40 most common words

# Average sentence length, frequency of long words

sentcount = wfreq['.'] + wfreq['?'] + wfreq['!']  # Assuming every sentence ends with ., ! or ?
print("Number of Sentences :",sentcount)
print("Average sentence length in number of words :", len(wtokens)/sentcount)     # Average sentence length in number of words

#print([w for w in wfreq if len(w) >= 13])   # all 13+ character words

long = [w for w in wfreq if len(w) >= 13]
#for w in long :
    #print(w, len(w), wfreq[w])               # long words tend to be less frequent

basecloud = WordCloud().generate(words)
plt.imshow(basecloud)
plt.axis("off")
plt.show()

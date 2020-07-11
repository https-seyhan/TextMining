import os
#import pandas as pd
#import spacy
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

os.chdir('/home/saul/pythontraining/NLP')

with open('journal.txt', 'r') as file:
    journal = file.read()

#print(journal)

stop_words = set(stopwords.words("english"))
#print(stop_words)

#word tokenize
word_tk = word_tokenize(journal)
#remove stopwords
clean_text = [word for word in word_tk if not word in stop_words]
print(len(journal))
print(len(clean_text))
print(len(journal) - len(clean_text))
#remove stop words
#cleaned_text = stopwords(journal)
print(clean_text)

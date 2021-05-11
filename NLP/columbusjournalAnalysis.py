import os
import re
import pandas as pd
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist

from matplotlib import pyplot as plt

figsize = (1500 / 50, 400 / 50)
wordfreqs =[['', '']]
os.chdir('/home/saul/pythontraining/NLP')

def nlpWork():

    with open('journal.txt', 'r') as file:
        journal = file.read()
    # remove numbers
    journal = re.sub(r'\d+', '', journal)
    stop_words = set(stopwords.words("english"))
    #word tokenize
    word_tk = word_tokenize(journal)
    #remove stopwords
    clean_text = [word for word in word_tk if not word in stop_words]
    #remove punctuation
    clean_text = [word for word in clean_text if word.isalnum()]
    wordAnalysis(clean_text)

def wordAnalysis(clean_text):
    #plot word distribution
    fd = FreqDist(clean_text)
    freqs = fd.most_common()
    for words in range(len(freqs)):
        wordfreqs.append([freqs[words][0], freqs[words][1]])
        if freqs[words][0] == 'God':
            print(freqs[words][0], freqs[words][1])
    #move words and their freq into dataframe
    topwords = pd.DataFrame(wordfreqs, columns=['Word', 'Freq'])
    topwords.to_csv('ColumbusWordFreq.csv', sep=",", header=True, index=False)
    fd.plot(50, cumulative=False)
    plt.show()

if __name__ == '__main__':
    nlpWork()


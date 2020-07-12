import os
import re
import pandas as pd
#import spacy
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
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
    stop_words.add('The') # add additional stop words
    stop_words.add('THE')  # add additional stop words
    stop_words.add('de')
    stop_words.add('one')
    stop_words.add('two')
    stop_words.add('It')

    #word tokenize
    word_tk = word_tokenize(journal)
    #remove stopwords
    clean_text = [word for word in word_tk if not word in stop_words]
    #remove punctuation
    clean_text = [word for word in clean_text if word.isalnum()]
    #lemmWords(clean_text)
    #wordAnalysis(clean_text)
    nlpVectorisation(journal, stop_words)

def lemmWords(clean_text):
    lemm_words = []
    lem = WordNetLemmatizer()
    for i in range(len(clean_text)):
        lemm_words.append(lem.lemmatize(clean_text[i]))

    #print("Lemminized Words ", lemm_words)
    fd = FreqDist(lemm_words)
    freqs = fd.most_common()
    #print(freqs)
    fd.plot(50, cumulative=False)
    plt.show()

def nlpVectorisation(journal, stop_words):
    #print("Vectors")

    #ger senstence token
    sentence_tk = sent_tokenize(journal)
    # remove stopwords
    clean_text = [sent for sent in sentence_tk if not sent in stop_words]
    clean_text= [x.replace('\n', '') for x in clean_text]

    #tf-idf
    vectorizer = TfidfVectorizer(min_df=1)
    model = vectorizer.fit_transform(clean_text)

    #print("Model Values ", len(model[0].todense()))
    wordweights = model[0].data

    words = clean_text[0].split(" ")

    dict = {}
    for word in range(len(wordweights)):
        print(wordweights[word])
        print(words[word])
        dict[words[word]] = wordweights[word]
    print("dictionary ", dict)


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


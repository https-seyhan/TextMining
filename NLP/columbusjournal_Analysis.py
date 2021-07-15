import os
import re
import pandas as pd
import operator
#import spacy
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from itertools import islice
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
    stop_words.add('be')
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
    fd.plot(50, cumulative=False)
    plt.show()

def nlpVectorisation(journal, stop_words):
    #print("Vectors")
    stop_words.add('one')
    stop_words.add('two')
    stop_words.add('It')
    #get sentence token
    sentence_tk = sent_tokenize(journal)
    # remove stopwords
    clean_text = []
    
    for sent in sentence_tk:
        clean_text.append(' '.join(w for w in nltk.word_tokenize(sent) if w.lower() not in stop_words))
    #clean_text = [sent for sent in sentence_tk if not sent in stop_words]
    clean_text = [x.replace('\n', '') for x in clean_text]
  
    #tf-idf
    vectorizer = TfidfVectorizer(min_df=1)
    model = vectorizer.fit_transform(clean_text)
    sentenceCount = 0
    
    while len(clean_text) > sentenceCount:
        getPurpose(model, clean_text, sentenceCount)
        sentenceCount += 1

def getPurpose(model, clean_text, sentenceNum):
    # print("Model Values ", len(model[0].todense()))
    # get weights of words
    wordweights = model[sentenceNum].data
    words = clean_text[sentenceNum].split(" ")
    sentencepurpose = {}
    #get tfidf vectors and insert into a dictionary
    for word in range(len(wordweights)): 
        print(words[word])
        sentencepurpose[words[word]] = wordweights[word]
    sentencepurpose = dict(sorted(sentencepurpose.items(), key=operator.itemgetter(1), reverse=True))
    #print("Purpose ", sentencepurpose)
    top_3_words = list(sentencepurpose)[:3]
    print("Purpose ", top_3_words)

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

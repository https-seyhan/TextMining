#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: saul
"""
# Extact text from images and then perform NLP on extracted text
import os
from PIL import Image as PI
from pytesseract import image_to_string # scrap text from images using pytesseract module
import pytesseract
from sklearn.feature_extraction.text import CountVectorizer # Convert text document to a matrix of token counts
import spacy # NLP framework 
import PyPDF2
from os import listdir
from os.path import isfile, join

receipt_data = {} # Dictionary of receipts
tesseract_cmd = 'tesseract'

os.chdir('/home/saul/pythontraining/NLP')



def convertImageString():
    a = PI.open("receipt_preview.jpg")
    #print(image_to_string(a))
    receipt_data['receipt'] = image_to_string(a)
    for x in receipt_data:
        spaCYWork([receipt_data[x]])

def NLPWork():
        vec = CountVectorizer()
        vec.fit(receipt_data)
        #two n-gram
        cv = CountVectorizer(ngram_range=(1,2)).fit(receipt_data)
        for x in receipt_data:

            vec.fit([receipt_data[x]])
            bag_of_words = vec.transform([receipt_data[x]])
            print("bag_of_words: {}".format(repr(bag_of_words)))
            #print("Dense respresntstion of bag_of_words:\n{}".format(bag_of_words.toarray()))
            feature_names = vec.get_feature_names()
            print("Number of features: {}".format(len(feature_names)))
            print("Feature names:\n{}".format(feature_names))
            
            bag_of_words2 = cv.transform([receipt_data[x]])
            print("bag_of_words2: {}".format(repr(bag_of_words2)))
        
        #print("Vocabulary size : {}".format(len(vec.vocabulary_)))
        #print("Vocabulary content:\n {}".format(vec.vocabulary_))
def spaCYWork(doc):
    print(doc)
    #print(receipt_data)
    #python3 -m spacy download en
    en_nlp = spacy.load('en')
    doc_spacy=en_nlp(doc)

        
if __name__ == '__main__':
    convertImageString()
    #print(receipt_data)
    #NLPWork()
    #spaCYWork()
    

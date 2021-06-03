#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: saul
"""
import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB 

os.chdir('/home/saul/pythonWork/NLP/Chapter_5/Data')
vec = CountVectorizer(min_df =0.001, max_df=0.95) # Convert a collection of text documents to a matrix of token counts

report = pd.read_csv('prReports.csv', encoding='utf-8')
print(len(report.columns))

#clf = MultinomialNB()
X = report['Description:'].values
print(X[0])
y= report['Warning:']
print(pd.crosstab(index=report['Warning:'],columns='count'))

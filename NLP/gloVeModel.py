#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: saul
"""
#GloVe model implementation in Python
from glove import Corpus, Glove

# creating a corpus object
corpus = Corpus()
#training the corpus to generate the cooccurence matrix which is used in GloVe
corpus.fit(lines, window=10)
#creating a Glove object which will use the matrix created in the above lines to create embeddings
#We can set the learning rate as it uses Gradient Descent and number of components

glove = Glove(no_components=5, learning_rate=0.05)
glove.fit(corpus.matrix, epochs=30, no_threads=4, verbose=True)
glove.add_dictionary(corpus.dictionary)
glove.save('glove.model')

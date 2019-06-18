# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import spacy

nlp = spacy.load('en_core_web_md')
tokens = nlp(u'car toyota milk')

for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)
    

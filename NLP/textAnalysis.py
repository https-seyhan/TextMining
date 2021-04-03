#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: saul
"""

import re

text = """Hey diddle diddle, We are all on the fiddle,
          And never get up until noon, We only takr cash, """

#Sub
#print(re.sub('We', 'They', text))

#Findall
          #{4,6} 4 to 6 in a row
#print(re.findall(r"[a-zA-Z]{4,6}", text))

#+ 1 or more * = 0 or mpre repetitives
#print(re.findall(r'n[o|e][a-z]*', text))

#() Indicates grouping \w and letter
#print(re.findall(r'([\w]+)dd([\w]+)', text))

#Search
#return first match only in the groups
a = re.search(r'([\w]+)dd([\w]+)', text)
#print(a.group(0), a.group(1), a.group(2))

#using compile
re_1 = re.compile(r'We')
re_2 = re.compile(r'n[o|e][a-z]*')

print(re_1.sub('They', text))
print(re_2.findall(text))

def square_function(x):
    return x * x

#using lambda
square_lamb = lambda x:x*x

print (square_function(5))
print (square_lamb(5))

#https://github.com/explosion/spacy-models/releases//tag/en_core_web_md-2.1.0


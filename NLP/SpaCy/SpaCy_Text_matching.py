#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: saul
"""
import plac
from spacy.lang.en import English
from spacy.matcher import PhraseMatcher, Matcher
from spacy.tokens import Doc, Span, Token
import spacy

nlp = spacy.load("en_core_web_sm")

text = """
    "Net income was $9.4 million compared to the prior year of $2.7 million.",
    "Revenue exceeded twelve billion dollars, with a loss of $1b. run",
"""
doc = nlp(text)
#print("Tokens", [t.text for t in doc])

#Every word in the text is a token
#print(doc.text[0])
#print(doc.text[1])
#print("Tags", [(t.text, t.tag_, t.pos_) for t in doc],'\n\n')
#print("Tokens", [t.text for t in doc],'\n')
 
#remove stop wods and verbs
cleantext = [t.text for t in doc if not t.is_stop and t.pos_ != 'VERB']
print(cleantext) 

#cleandoc = nlp(Doc(nlp.vocab, cleantext))
# convert list ot nlp doc
cleandoc = Doc(nlp.vocab, words=cleantext)
print("cleandoc ", cleandoc)
matcher = Matcher(nlp.vocab)
# Add match ID "item" with no callback and one pattern
pattern1 = [{"LOWER": "compared"}]
pattern2 = [{"LOWER": "description"}]
pattern3 = [{"LOWER": "prior"}]
matcher.add("item", None, pattern1, pattern2, pattern3)
matches = matcher(cleandoc)

word_list = []
word_dict = {}
print(matches)

for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = cleandoc[start:end]  # The matched span
    print(start, end, span.text)
    word_dict[span.text] = {} # create dictionary for keyword
    word_dict[span.text][cleandoc[start-1]] = -1

    #print(doc[start-1])
    word_list.append(cleandoc[start-1])
    #print(doc[start-2])
    #word_dict[span.text].([cleandoc[start-2]])
    word_dict[span.text][cleandoc[start-2]] = -2
                                
    word_list.append(cleandoc[start-2])
    #print(doc[start-3])
    word_dict[span.text][cleandoc[start-3]] = -3
    
    word_list.append(cleandoc[start-3])
    #print(doc[start-4])
    word_dict[span.text][cleandoc[start-4]] = -4
    word_list.append(cleandoc[start-4])
    
    #print(doc[start-5],'\n')
    word_dict[span.text][cleandoc[start-5]] = -5
    word_list.append(cleandoc[start-5])
    #print(doc[start+1])
    word_dict[span.text][cleandoc[start+1]] = 1
    word_list.append(cleandoc[start + 1])
    #print(doc[start+2])
    word_dict[span.text][cleandoc[start+2]] = 2
    word_list.append(cleandoc[start + 2])
    #print(doc[start+3])
    word_dict[span.text][cleandoc[start+3]] = 3
    word_list.append(cleandoc[start + 3])
    #print(doc[start+4])
    
    word_dict[span.text][cleandoc[start+4]] = 4
    word_list.append(cleandoc[start + 4])
    #print(doc[start+5],'\n')
    word_dict[span.text][cleandoc[start+5]] = 5
    word_list.append(cleandoc[start + 5])
    print(word_list)
    print(word_dict)

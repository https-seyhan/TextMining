#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: saul
"""
import plac
import spacy
import pandas as pd
import re
from spacy.matcher import Matcher
from spacy.tokens import Doc

nlp = spacy.load("en_core_web_sm")

customize_stop_words = [
    'From', 'To'
]
for w in customize_stop_words:
    nlp.vocab[w].is_stop = True

def getItem(receipt):
     

    text = """
    "Net income was $9.4 million compared to the prior year of $2.7 million.",
    "Revenue exceeded twelve billion dollars, with a loss of $1b. run",
    """
    text = receipt.strip("n\n")
    text = receipt.strip("\\n")
    
    text = re.sub(r"[\'?'\n\'[]:]","",text, flags=re.I)
    #text = re.sub("\n","", text)
    #text.replace(r"['\n']", '')
    
    #text = ', '.join(text)
    #text = text.replace('"', '')
    #text = text.replace('\n', '')
    #print (mylist)

    
    #print("Text ", type(text))
    #print("Text :", text)
    doc = nlp(text)
#print("Tokens", [t.text for t in doc])

#Every word in the text is a token
#print(doc.text[0])
#print(doc.text[1])
#print("Tags", [(t.text, t.tag_, t.pos_) for t in doc],'\n\n')
#print("Tokens", [t.text for t in doc],'\n')
 

#remove stop wods and verbs
    cleantext = [t.text for t in doc if not t.is_stop and t.pos_ == 'NOUN']
    print("Clean Text ", cleantext) 

#cleandoc = nlp(Doc(nlp.vocab, cleantext))
# convert list to nlp doc
    cleandoc = Doc(nlp.vocab, words=cleantext)
    #print("cleandoc ", cleandoc)
    matcher = Matcher(nlp.vocab)
# Add match ID "item" with no callback and one pattern
    pattern1 = [{"LOWER": "compared"}]
    pattern2 = [{"LOWER": "description"}]
    pattern3 = [{"LOWER": "prior"}]
    pattern4 = [{"LOWER": "receipt"}]
    matcher.add("item", None, pattern1, pattern2, pattern3, pattern4)
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
        
def getText():
    text2 = pd.read_csv('/home/saul/pythontraining/NLP/imagetotext.csv')
    
    #get a line 
    mytext = text2.iloc[[1]]
    receipt = mytext.iloc[0].text
    #print(receipt)
    #print(type(receipt))
    getItem(receipt)
        

getText()
    #getItem()


# In[57]:


mylist=['"Newyork"\n', '"Teacher2"', '"A"']
mylist = ', '.join(mylist)
mylist = mylist.replace('"', '')
mylist = mylist.replace('\n', '')
print (mylist)



# In[6]:


print(type(receipt))


# In[ ]:
Clean Text  ['Receipt', 'travel', 'fae', 'PC', 'travel', 'tours', 'seaters', 'hire', 'rail', 'cars', 'Airport', 'prioity', 'meet', 'ores', 'xury', 'executive', 'travel\\n\\nVISA', 'eta', '\\n\\nfees)\\n\\nanmojorcards', 'wing', 'EXCELLENCE', 'HIGHLANDS']
[(9788585321747494026, 0, 1)]
0 1 Receipt
[HIGHLANDS, EXCELLENCE, wing, \n\nfees)\n\nanmojorcards, eta, travel, fae, PC, travel, tours]
{'Receipt': {HIGHLANDS: -1, EXCELLENCE: -2, wing: -3, \n\nfees)\n\nanmojorcards: -4, eta: -5, travel: 1, fae: 2, PC: 3, travel: 4, tours: 5}}




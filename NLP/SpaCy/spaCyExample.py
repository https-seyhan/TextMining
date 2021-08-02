#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: saul
"""
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

# In[3]:

doc = nlp('European authorities fined Google tax receipt a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
print([(X.text, X.label_) for X in doc.ents])

# In[4]:
print([(X, X.ent_iob_, X.ent_type_) for X in doc])


# In[9]:
from bs4 import BeautifulSoup
import requests
import re

def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))

ny_bb = url_to_string('https://www.nytimes.com/2018/08/13/us/politics/peter-strzok-fired-fbi.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news')
article = nlp(ny_bb)
len(article.ents)


# In[10]:

labels = [x.label_ for x in article.ents]
Counter(labels)


# In[7]:

doc2 = nlp("receipt Quantity")


# In[8]:

print([(X.text, X.label_) for X in doc2.ents])


# In[15]:


print([(X.text, X.label_) for X in article.ents])


# In[17]:


labels


# In[18]:


items = [x.text for x in article.ents]
Counter(items).most_common(3)


# In[22]:


sentences = [x for x in article.sents]
print(sentences[20])


# In[23]:


displacy.render(nlp(str(sentences[20])), jupyter=True, style='ent')


# In[24]:


displacy.render(nlp(str(sentences[20])), style='dep', jupyter = True, options = {'distance': 120})


# In[25]:


[(x.orth_,x.pos_, x.lemma_) for x in [y 
                                      for y
                                      in nlp(str(sentences[20])) 
                                      if not y.is_stop and y.pos_ != 'PUNCT']]


# In[26]:


dict([(str(x), x.label_) for x in nlp(str(sentences[20])).ents])


# In[27]:


print([(x, x.ent_iob_, x.ent_type_) for x in sentences[20]])


# In[ ]:


# 

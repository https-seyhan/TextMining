import plac
from spacy.lang.en import English
from spacy.matcher import PhraseMatcher
from spacy.tokens import Doc, Span, Token

nlp = English()
# remove stop words
# seach pattern1 and pattern2 in text using Python spaCy
# get the location of pattern1 and pattern2
# get the prior 5 and previous 5 words around pattern1 and pattern2

text = """
    "Net income was $9.4 million compared to the prior year of $2.7 million.",
    "Revenue exceeded twelve billion dollars, with a loss of $1b.",
"""
doc = nlp(text)
print("Tokens", [t.text for t in doc])

#Every word in the text is a token
print(doc.text[0])
print(doc.text[1])
print("Tags", [(t.text, t.tag_, t.pos_) for t in doc])
print("Tokens", [t.text for t in doc if not t.is_stop])

#create matcher
matcher = Matcher(nlp.vocab)
# Add match ID "item" with no callback and one pattern
pattern1 = [{"LOWER": "compared"}]
pattern2 = [{"LOWER": "description"}]
matcher.add("item", None, pattern1, pattern2)
matches = matcher(doc)
word_list = []

for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = doc[start:end]  # The matched span
    print(start, end, span.text)
    print(doc[start-1])
    word_list.append(doc[start-1])
    print(doc[start-2])
    word_list.append(doc[start-2])
    print(doc[start-3])
    word_list.append(doc[start-3])
    print(doc[start-4])
    word_list.append(doc[start-4])
    print(doc[start-5],'\n')
    word_list.append(doc[start-5])
    print(doc[start+1])
    word_list.append(doc[start + 1])
    print(doc[start+2])
    word_list.append(doc[start + 2])
    print(doc[start+3])
    word_list.append(doc[start + 3])
    print(doc[start+4])
    word_list.append(doc[start + 4])
    print(doc[start+5],'\n')
    word_list.append(doc[start + 5])
print(word_list)
 
   
#p1 = [{'LOWER': 'quickbrownfox'}]  
#p2 = [{'LOWER': 'quick'}, {'IS_PUNCT': True}, {'LOWER': 'brown'}, {'IS_PUNCT': True}, {'LOWER': 'fox'}]  
#p3 = [{'LOWER': 'quick'}, {'LOWER': 'brown'}, {'LOWER': 'fox'}]  
#p4 =  [{'LOWER': 'quick'}, {'LOWER': 'brownfox'}]  
#    p1 looks for the phrase "quickbrownfox"
#    p2 looks for the phrase "quick-brown-fox"
#    p3 tries to search for "qucik brown fox"
#    p4 looks for the phrase "quick brownfox"

#load spacy
import spacy
nlp = spacy.load("en_core_web_lg")
text = "iPhones."
doc = nlp(text)
for ent in doc.ents:
    if ent.label_ == "PRODUCT":
        print(ent.text, ent.start_char, ent.end_char, ent.label_)

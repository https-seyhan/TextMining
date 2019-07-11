import plac
from spacy.lang.en import English
from spacy.matcher import PhraseMatcher, Matcher
from spacy.tokens import Doc, Span, Token
import spacy

nlp = spacy.load("en_core_web_sm")

text = """
    "Net income was $9.4 million acompared to the prior year of $2.7 million.",
    "Revenue exceeded twelve billion dollars, with a loss of $1b. run",
"""
doc = nlp(text)

pattern1 = [{"LOWER": "compared"}]
pattern = [{"LOWER": {"REGEX": "\b\w*compared\w*\b"}}]
#pattern3 = [{"LOWER": {"REGEX": "compared}}]

matcher = Matcher(nlp.vocab)
matcher.add("item", None,  pattern )
matches = matcher(doc)
print(matches)
print(matcher)

import re
re.findall("united", "123united")

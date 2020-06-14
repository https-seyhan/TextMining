import plac
from spacy.lang.en import English
from spacy.matcher import PhraseMatcher, Matcher
from spacy.tokens import Doc, Span, Token
import spacy

nlp = spacy.load("en_core_web_sm")

text = """
"Net income was $9.4 million acompared to the prior year of $2.7
million.",
"Revenue exceeded twelve billion dollars, with a loss of $1b. run",
"""

doc = nlp(text)

pattern = [{"LOWER": {"REGEX": "\\b\w*(?:compared)\w*\b"}}]
pattern = [{"TEXT": {"REGEX": "compared*"}}]

matcher = Matcher(nlp.vocab)
matcher.add("item", None, pattern )
matches = matcher(doc)
for match_id, start, end in matches:
  string_id = nlp.vocab.strings[match_id]  # Get string representation
  span = doc[start:end]  # The matched span
  print(start, end, span.text)
print(matches)
print(matcher)

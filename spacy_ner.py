import spacy

from spacy.matcher import Matcher

nlp = spacy.load("fr_core_news_sm")

matcher = Matcher(nlp.vocab)

pattern = [{"TEXT": "iPhone"}, {"TEXT": "12"}]
matcher.add("IPHONE_PATTERN", [pattern])

doc = nlp("La date de sortie du futur iPhone 12 a fuité")

matches = matcher(doc)

for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)
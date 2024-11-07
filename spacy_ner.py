import spacy

nlp = spacy.blank("fr")

from spacy.tokens import Doc, Span

words = ["Bonjour", "monde", "!"]
spaces = [True, True, False]

doc = Doc(nlp.vocab, words=words, spaces=spaces)

span = Span(doc, 0, 2)

span_with_label = Span(doc, 0, 2, label="GREETING")

doc.ents = [span_with_label]

print(doc.text)
print(span.text)
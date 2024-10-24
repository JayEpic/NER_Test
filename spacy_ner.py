import spacy

nlp = spacy.load("fr_core_news_sm")

doc = nlp("Ines nage souvent")
print("valeur de hash :", nlp.vocab.strings["souvent"])

print("valeur de chaîne :", nlp.vocab.strings[821433950267086228])
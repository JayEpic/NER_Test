import spacy
nlp = spacy.load("fr_core_news_sm")

doc = nlp("Apple conçoit le nouvel iPhone à Cupertino.")

for ent in doc.ents:
    print(ent.text, ent.label_)
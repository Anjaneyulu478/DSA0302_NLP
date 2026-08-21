import spacy

nlp = spacy.load("en_core_web_sm")

text = "Ravi works at Microsoft in Chennai."

doc = nlp(text)

print("Named Entities:")
for ent in doc.ents:
    print(ent.text, "-", ent.label_)

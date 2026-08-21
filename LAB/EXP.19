from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

sentence = "I went to the bank to deposit money"

sense = lesk(word_tokenize(sentence), "bank")

print("Word:", "bank")

if sense:
    print("Meaning:", sense.definition())
else:
    print("Sense not found")

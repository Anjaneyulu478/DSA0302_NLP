from nltk.corpus import wordnet

word = "computer"

synsets = wordnet.synsets(word)

print("Synsets:")
for syn in synsets:
    print(syn.name())
    print("Meaning:", syn.definition())
    print()

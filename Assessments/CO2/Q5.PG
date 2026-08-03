from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["relational", "relation", "relate"]

print("-"*95)
print("{:<15}{:<20}{:<20}{:<15}".format(
    "Word","Applied Rule","Intermediate","Final Stem"))
print("-"*95)

for word in words:

    if word == "relational":
        rule = "Remove -ational"
        intermediate = "relate"

    elif word == "relation":
        rule = "Remove -ion"
        intermediate = "relate"

    elif word == "relate":
        rule = "No major change"
        intermediate = "relate"

    stem = ps.stem(word)

    print("{:<15}{:<20}{:<20}{:<15}".format(
        word,rule,intermediate,stem))

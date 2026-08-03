words = ["played", "player", "playing"]

print("-"*85)
print("{:<15}{:<12}{:<15}{:<15}{:<15}".format(
    "Word","Stem","Removed Affix","Type","Normalized"))
print("-"*85)

for word in words:

    if word.endswith("ed"):
        stem = "play"
        affix = "ed"
        t = "Inflectional"

    elif word.endswith("ing"):
        stem = "play"
        affix = "ing"
        t = "Inflectional"

    elif word.endswith("er"):
        stem = "play"
        affix = "er"
        t = "Derivational"

    print("{:<15}{:<12}{:<15}{:<15}{:<15}".format(
        word,stem,affix,t,stem))

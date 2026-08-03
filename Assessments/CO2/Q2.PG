# Morphological Parsing Module

words = ["unhappy", "happiness", "happily"]

print("-" * 110)
print("{:<15}{:<12}{:<15}{:<15}{:<18}{:<15}".format(
    "Word", "Prefix", "Root", "Suffix", "Transformation", "Normalized"))
print("-" * 110)

for word in words:

    prefix = "-"
    suffix = "-"
    root = word
    trans = "Base"

    if word.startswith("un"):
        prefix = "un"
        root = word[2:]
        trans = "Derivational"

    elif word.endswith("ness"):
        suffix = "ness"
        root = word[:-4] + "y"
        trans = "Derivational"

    elif word.endswith("ly"):
        suffix = "ly"
        root = word[:-2] + "y"
        trans = "Derivational"

    print("{:<15}{:<12}{:<15}{:<15}{:<18}{:<15}".format(
        word, prefix, root, suffix, trans, "happy"))

print("-" * 110)

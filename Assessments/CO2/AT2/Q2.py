# Experiment 2: Morphological Parsing

words = ["disagree", "agreement", "agreeable"]

for word in words:
    prefix = "-"
    suffix = "-"
    root = "agree"
    morph_type = ""
    meaning = ""

    if word.startswith("dis"):
        prefix = "dis-"
        morph_type = "Derivational"
        meaning = "Negative meaning"

    elif word.endswith("ment"):
        suffix = "-ment"
        morph_type = "Derivational"
        meaning = "State or result"

    elif word.endswith("able"):
        suffix = "-able"
        morph_type = "Derivational"
        meaning = "Capable of"

    print("Original Word :", word)
    print("Prefix        :", prefix)
    print("Root          :", root)
    print("Suffix        :", suffix)
    print("Type          :", morph_type)
    print("Meaning       :", meaning)
    print("Normalized    :", root)
    print("-" * 40)

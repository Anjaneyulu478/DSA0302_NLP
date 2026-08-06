# Experiment 4: Morphological Parsing

words = ["activate", "activation", "reactivation"]

for word in words:
    prefix = "-"
    suffix = "-"
    root = "activate"
    sequence = ""

    if word == "activate":
        sequence = "Base Form"

    elif word == "activation":
        suffix = "-ion"
        sequence = "activate + ion"

    elif word == "reactivation":
        prefix = "re-"
        suffix = "-ion"
        sequence = "re + activate + ion"

    print("Original Word :", word)
    print("Prefix        :", prefix)
    print("Root          :", root)
    print("Suffix        :", suffix)
    print("Sequence      :", sequence)
    print("Normalized    :", root)
    print("-" * 40)

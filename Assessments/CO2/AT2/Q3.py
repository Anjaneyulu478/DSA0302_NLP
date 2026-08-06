# Experiment 3: Morphological Normalization

words = ["govern", "government", "governance"]

for word in words:
    root = "govern"
    suffix = "-"
    level = "Base"

    if word == "government":
        suffix = "-ment"
        level = "Level 1"

    elif word == "governance":
        suffix = "-ance"
        level = "Level 1"

    print("Original Word :", word)
    print("Root          :", root)
    print("Suffix        :", suffix)
    print("Hierarchy     :", level)
    print("Normalized    :", root)
    print("-" * 40)

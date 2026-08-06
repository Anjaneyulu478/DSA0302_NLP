# Experiment 5: Inflectional Morphology Normalization

words = ["create", "creates", "creating"]

for word in words:
    suffix = "-"
    category = ""

    if word == "create":
        category = "Base Form"

    elif word.endswith("s"):
        suffix = "-s"
        category = "Third Person Singular"

    elif word.endswith("ing"):
        suffix = "-ing"
        category = "Present Participle"

    print("Original Word :", word)
    print("Suffix        :", suffix)
    print("Category      :", category)
    print("Root          :", "create")
    print("Normalized    :", "create")
    print("-" * 40)

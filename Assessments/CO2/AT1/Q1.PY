  words = ["connected", "connecting", "connection"]

rules = {
    "ed": ("connect", "ed", "Inflectional"),
    "ing": ("connect", "ing", "Inflectional"),
    "ion": ("connect", "ion", "Derivational")
}

print("-" * 70)
print("{:<15} {:<12} {:<10} {:<15} {:<15}".format(
    "Word", "Root", "Suffix", "Type", "Normalized"))
print("-" * 70)

for word in words:
    for suffix in rules:
        if word.endswith(suffix):
            root, suf, t = rules[suffix]
            print("{:<15} {:<12} {:<10} {:<15} {:<15}".format(
                word, root, suf, t, root))
            break

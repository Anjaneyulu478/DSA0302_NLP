# Rule-Based Morphological Processing System

# Input words
words = ["analyzing", "analysis", "analytical"]

# Rule dictionary
morphology_rules = {
    "analyzing": {
        "root": "analyze",
        "affix": "-ing",
        "type": "Inflectional",
        "normalized": "analyze"
    },
    "analysis": {
        "root": "analyze",
        "affix": "-sis",
        "type": "Derivational",
        "normalized": "analyze"
    },
    "analytical": {
        "root": "analyze",
        "affix": "-ical",
        "type": "Derivational",
        "normalized": "analyze"
    }
}

# Print Report
print("=" * 95)
print("{:<15} {:<15} {:<12} {:<18} {:<25} {:<15}".format(
    "Original",
    "Root",
    "Affix",
    "Transformation",
    "Morphological Structure",
    "Normalized"
))
print("=" * 95)

for word in words:
    info = morphology_rules[word]

    structure = info["root"] + " + " + info["affix"].replace("-", "")

    print("{:<15} {:<15} {:<12} {:<18} {:<25} {:<15}".format(
        word,
        info["root"],
        info["affix"],
        info["type"],
        structure,
        info["normalized"]
    ))

print("=" * 95)

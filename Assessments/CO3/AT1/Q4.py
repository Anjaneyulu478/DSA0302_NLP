import re
from collections import Counter, defaultdict

sentence = "The student is reading a book"

words = sentence.lower().split()

def rule_based_tagger(words):

    tags = []

    for word in words:

        if word in ["the", "a", "an"]:
            tag = "DT"

        elif word in ["is", "am", "are", "was", "were"]:
            tag = "VBZ"

        elif word.endswith("ing"):
            tag = "VBG"

        elif word.endswith("ly"):
            tag = "RB"

        elif word in ["i", "you", "he", "she", "we", "they"]:
            tag = "PRP"

        else:
            tag = "NN"

        tags.append((word, tag))

    return tags

training_data = [
    ("the", "DT"),
    ("student", "NN"),
    ("teacher", "NN"),
    ("is", "VBZ"),
    ("reading", "VBG"),
    ("writing", "VBG"),
    ("a", "DT"),
    ("book", "NN"),
    ("quickly", "RB")
]

word_tags = defaultdict(Counter)

for word, tag in training_data:
    word_tags[word][tag] += 1


def stochastic_tagger(words):

    result = []

    for word in words:

        if word in word_tags:
            tag = word_tags[word].most_common(1)[0][0]
        else:
            tag = "NN"

        result.append((word, tag))

    return result

def transformation_tagger(words):

    result = [(word, "NN") for word in words]

    for i, (word, tag) in enumerate(result):
        if word in ["the", "a", "an"]:
            result[i] = (word, "DT")

        elif word in ["is", "am", "are", "was", "were"]:
            result[i] = (word, "VBZ")

        elif word.endswith("ing"):
            result[i] = (word, "VBG")

        elif word.endswith("ly"):
            result[i] = (word, "RB")

    return result

print("Sentence:")
print(sentence)

print("\nRule-Based POS Tagging:")
for word, tag in rule_based_tagger(words):
    print(word, "->", tag)

print("\nStochastic POS Tagging:")
for word, tag in stochastic_tagger(words):
    print(word, "->", tag)

print("\nTransformation-Based Tagging:")
for word, tag in transformation_tagger(words):
    print(word, "->", tag)

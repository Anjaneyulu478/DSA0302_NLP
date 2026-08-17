from collections import Counter
import math
import re

train_text = """
the student is reading a book
the student is learning python
the teacher is reading a book
the teacher is teaching python
"""

test_text = """
the student is learning
the teacher is reading
"""

train = re.findall(r'\b\w+\b', train_text.lower())
test = re.findall(r'\b\w+\b', test_text.lower())

unigram = Counter(train)

bigram = Counter(
    (train[i], train[i+1])
    for i in range(len(train)-1)
)

trigram = Counter(
    (train[i], train[i+1], train[i+2])
    for i in range(len(train)-2)
)

def calculate_unigram_entropy(test):
    entropy = 0
    count = 0

    for word in test:

        probability = unigram[word] / len(train)

        if probability > 0:
            entropy -= math.log2(probability)
            count += 1

    return entropy / count


def calculate_bigram_entropy(test):
    entropy = 0
    count = 0

    for i in range(1, len(test)):

        previous = test[i-1]
        current = test[i]

        denominator = unigram[previous]
        numerator = bigram[(previous, current)]

        if denominator > 0 and numerator > 0:

            probability = numerator / denominator

            entropy -= math.log2(probability)
            count += 1

    return entropy / count

def calculate_trigram_entropy(test):
    entropy = 0
    count = 0

    for i in range(2, len(test)):

        w1 = test[i-2]
        w2 = test[i-1]
        w3 = test[i]

        denominator = bigram[(w1, w2)]
        numerator = trigram[(w1, w2, w3)]

        if denominator > 0 and numerator > 0:

            probability = numerator / denominator

            entropy -= math.log2(probability)
            count += 1

    return entropy / count


print("Unigram Entropy:",
      round(calculate_unigram_entropy(test), 4))

print("Bigram Entropy:",
      round(calculate_bigram_entropy(test), 4))

print("Trigram Entropy:",
      round(calculate_trigram_entropy(test), 4))

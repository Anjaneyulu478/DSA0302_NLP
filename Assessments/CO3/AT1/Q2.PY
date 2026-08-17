from collections import Counter
import re

corpus = """
the student is studying
the student is reading
the student likes books
the teacher is teaching
the teacher likes books
the student likes learning
"""

tokens = re.findall(r'\b\w+\b', corpus.lower())

unigram = Counter(tokens)

bigram = Counter(
    (tokens[i], tokens[i+1])
    for i in range(len(tokens)-1)
)

trigram = Counter(
    (tokens[i], tokens[i+1], tokens[i+2])
    for i in range(len(tokens)-2)
)

def unigram_prob(word):
    return unigram[word] / len(tokens)

def bigram_prob(w1, w2):
    denominator = unigram[w1]

    if denominator == 0:
        return 0

    return bigram[(w1, w2)] / denominator

def trigram_prob(w1, w2, w3):
    denominator = bigram[(w1, w2)]

    if denominator == 0:
        return 0

    return trigram[(w1, w2, w3)] / denominator


def backoff(w1, w2, w3):
    p3 = trigram_prob(w1, w2, w3)

    if p3 > 0:
        return p3, "Trigram"

    p2 = bigram_prob(w2, w3)

    if p2 > 0:
        return p2, "Bigram"

    p1 = unigram_prob(w3)

    return p1, "Unigram"

def interpolation(w1, w2, w3):
    lambda3 = 0.5
    lambda2 = 0.3
    lambda1 = 0.2

    p3 = trigram_prob(w1, w2, w3)
    p2 = bigram_prob(w2, w3)
    p1 = unigram_prob(w3)

    probability = (
        lambda3 * p3 +
        lambda2 * p2 +
        lambda1 * p1
    )

    return probability

context = ("the", "student")

vocabulary = set(tokens)

print("===== PREDICTIONS =====")

results = []

for word in vocabulary:

    p_tri = trigram_prob(context[0], context[1], word)

    p_back, model = backoff(
        context[0],
        context[1],
        word
    )

    p_interp = interpolation(
        context[0],
        context[1],
        word
    )

    results.append(
        (word, p_tri, p_back, model, p_interp)
    )

results.sort(key=lambda x: x[4], reverse=True)

for word, p_tri, p_back, model, p_interp in results[:5]:

    print("\nWord:", word)
    print("Unsmoothed Trigram:", round(p_tri, 4))
    print("Backoff:", round(p_back, 4),
          "using", model)
    print("Interpolation:", round(p_interp, 4))

from collections import Counter
import re

corpus = """
the student is studying natural language processing
the student is reading a book
the student likes machine learning
the teacher is teaching natural language processing
the teacher likes machine learning
students are learning natural language processing
"""

tokens = re.findall(r'\b\w+\b', corpus.lower())

def get_ngrams(tokens, n):
    return [tuple(tokens[i:i+n])
            for i in range(len(tokens)-n+1)]

unigrams = get_ngrams(tokens, 1)
bigrams = get_ngrams(tokens, 2)
trigrams = get_ngrams(tokens, 3)

uni_count = Counter(unigrams)
bi_count = Counter(bigrams)
tri_count = Counter(trigrams)

print("===== UNIGRAM COUNTS =====")
for gram, count in uni_count.items():
    print(gram, ":", count)

print("\n===== BIGRAM COUNTS =====")
for gram, count in bi_count.items():
    print(gram, ":", count)

print("\n===== TRIGRAM COUNTS =====")
for gram, count in tri_count.items():
    print(gram, ":", count)

def bigram_probability(w1, w2):
    count_bigram = bi_count[(w1, w2)]
    count_word = uni_count[(w1,)]

    if count_word == 0:
        return 0

    return count_bigram / count_word

def trigram_probability(w1, w2, w3):
    count_trigram = tri_count[(w1, w2, w3)]
    count_bigram = bi_count[(w1, w2)]

    if count_bigram == 0:
        return 0

    return count_trigram / count_bigram

def predict_next(words, n):
    words = words.lower().split()

    if n == 1:
        candidates = []
        for (word,), count in uni_count.items():
            probability = count / len(tokens)
            candidates.append((word, probability))

    elif n == 2:
        previous = words[-1]
        candidates = []

        for (w1, w2), count in bi_count.items():
            if w1 == previous:
                probability = count / uni_count[(w1,)]
                candidates.append((w2, probability))

    elif n == 3:
        previous = tuple(words[-2:])
        candidates = []

        for (w1, w2, w3), count in tri_count.items():
            if (w1, w2) == previous:
                probability = count / bi_count[(w1, w2)]
                candidates.append((w3, probability))

    else:
        return []

    candidates.sort(key=lambda x: x[1], reverse=True)
    return candidates[:5]

query = "the student is"

print("\n===== TOP-5 NEXT WORD PREDICTIONS =====")

for n in [1, 2, 3]:
    print(f"\nN = {n}")
    predictions = predict_next(query, n)

    if predictions:
        for word, probability in predictions:
            print(f"{word:15} {probability:.4f}")
    else:
        print("No prediction available.")


print("\n===== UNSEEN BIGRAM =====")

probability = bigram_probability("student", "football")

print("P(football | student) =", probability)

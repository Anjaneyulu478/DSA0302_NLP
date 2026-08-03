import random
from nltk import word_tokenize, bigrams
from nltk.corpus import stopwords
import nltk

text = """
The cat sat on the mat.
The cat likes milk.
The dog sat on the floor.
The dog likes bones.
The cat and the dog are friends.
"""

tokens = word_tokenize(text.lower())

bigram_pairs = list(bigrams(tokens))

bigram_dict = {}

for w1, w2 in bigram_pairs:
    if w1 not in bigram_dict:
        bigram_dict[w1] = []
    bigram_dict[w1].append(w2)

def generate_text(start_word, length=15):
    word = start_word.lower()

    if word not in bigram_dict:
        return "Start word not found."

    sentence = [word]

    for _ in range(length - 1):
        next_words = bigram_dict.get(word)

        if not next_words:
            break

        word = random.choice(next_words)
        sentence.append(word)

    return " ".join(sentence)

start = "the"
generated = generate_text(start, 15)

print("Generated Text:")
print(generated)

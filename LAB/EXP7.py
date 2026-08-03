import nltk
from nltk import word_tokenize, pos_tag

text = "The quick brown fox jumps over the lazy dog."

words = word_tokenize(text)

tagged_words = pos_tag(words)

print("Part-of-Speech Tagging:\n")

for word, tag in tagged_words:
    print(f"{word:10} -> {tag}")

import random

words = input("Enter a sentence: ").split()

tags = ["NN", "VB", "JJ", "RB"]

for word in words:
    print(word, "->", random.choice(tags))

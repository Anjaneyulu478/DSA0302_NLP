from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = [
    "running",
    "playing",
    "happiness",
    "studies",
    "connected",
    "easily"
]

print("Original\tStemmed")

for word in words:
    print(word, "\t", ps.stem(word))

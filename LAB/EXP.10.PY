words = ["I", "am", "playing", "cricket"]

tags = ["NN", "NN", "NN", "NN"]

print("Before Transformation:")
print(list(zip(words, tags)))

for i in range(len(words)):
    if words[i].endswith("ing"):
        tags[i] = "VBG"

print("\nAfter Transformation:")
print(list(zip(words, tags)))

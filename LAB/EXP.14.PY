sentence = input("Enter a sentence: ")

words = sentence.split()

if len(words) >= 2:
    subject = words[0]
    verb = words[1]

    if subject.lower() in ["he", "she", "it"] and verb.endswith("s"):
        print("Agreement is Correct")
    elif subject.lower() in ["i", "we", "you", "they"] and not verb.endswith("s"):
        print("Agreement is Correct")
    else:
        print("Agreement is Incorrect")
else:
    print("Invalid Sentence")

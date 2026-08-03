import re

# Sample text
text = """
Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing
Python programming is useful for NLP applications.
"""

# Search Date
def search_date(text):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    return re.findall(pattern, text)


# Search Phone Number
def search_phone(text):
    pattern = r'\b[6-9]\d{9}\b'
    return re.findall(pattern, text)


# Search Hashtag
def search_hashtag(text):
    pattern = r'#[A-Za-z0-9_]+'
    return re.findall(pattern, text)


# Search Mention
def search_mention(text):
    pattern = r'@[A-Za-z0-9_]+'
    return re.findall(pattern, text)


# Prefix Search
def search_prefix(text, prefix):
    pattern = r'\b' + re.escape(prefix) + r'\w*'
    return re.findall(pattern, text, re.IGNORECASE)
# Suffix Search
def search_suffix(text, suffix):
    pattern = r'\b\w*' + re.escape(suffix) + r'\b'
    return re.findall(pattern, text, re.IGNORECASE)
# Word Search
def search_word(text, word):
    pattern = r'\b' + re.escape(word) + r'\b'
    return re.findall(pattern, text, re.IGNORECASE)
# Display text
print("----- TEXT -----")
print(text)
while True:
    print("\n----- SMART PATTERN MATCHING ENGINE -----")
    print("1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Search Word")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        result = search_date(text)
        print("\nMatching Dates:", result)

    elif choice == "2":
        result = search_phone(text)
        print("\nMatching Phone Numbers:", result)

    elif choice == "3":
        result = search_hashtag(text)
        print("\nMatching Hashtags:", result)

    elif choice == "4":
        result = search_mention(text)
        print("\nMatching Mentions:", result)

    elif choice == "5":
        prefix = input("Enter prefix: ")
        result = search_prefix(text, prefix)
        print("\nMatching Prefix Words:", result)

    elif choice == "6":
        suffix = input("Enter suffix: ")
        result = search_suffix(text, suffix)
        print("\nMatching Suffix Words:", result)
    elif choice == "7":
        word = input("Enter word: ")
        result = search_word(text, word)
        print("\nMatching Words:", result)
    elif choice == "8":
        print("\nExiting program...")
        break
    else:
        print("\nInvalid choice. Please try again.")

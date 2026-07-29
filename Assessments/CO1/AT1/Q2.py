import re

# -----------------------------------
# Product Database
# -----------------------------------

products = [
    "Apple iPhone 15",
    "Apple MacBook Air",
    "Samsung Galaxy S24",
    "Samsung Smart TV",
    "Dell Inspiron Laptop",
    "HP Pavilion Laptop",
    "Sony Headphones",
    "Boat Bluetooth Speaker",
    "Python Programming Book",
    "Java Programming Book",
    "SQL Database Book",
    "Machine Learning Guide",
    "NLP Essentials",
    "Wireless Mouse",
    "Gaming Keyboard"
]

# -----------------------------------
# Search Function
# -----------------------------------

def search_products(pattern, description):

    print("\n" + "=" * 50)
    print(description)
    print("=" * 50)

    matches = []

    for product in products:
        if re.search(pattern, product, re.IGNORECASE):
            matches.append(product)

    if matches:
        for item in matches:
            print(item)
    else:
        print("No matching products found.")

    print("Total Matches:", len(matches))


# -----------------------------------
# 1. Exact Keyword Search
# -----------------------------------

keyword = "Python Programming Book"
pattern = rf"^{re.escape(keyword)}$"
search_products(pattern, "1. Exact Keyword Search")

# -----------------------------------
# 2. Prefix Search
# -----------------------------------

prefix = "Apple"
pattern = rf"^{re.escape(prefix)}"
search_products(pattern, "2. Prefix Search")

# -----------------------------------
# 3. Suffix Search
# -----------------------------------

suffix = "Book"
pattern = rf"{re.escape(suffix)}$"
search_products(pattern, "3. Suffix Search")

# -----------------------------------
# 4. Partial Keyword Search
# -----------------------------------

partial = "Laptop"
pattern = rf"{re.escape(partial)}"
search_products(pattern, "4. Partial Keyword Search")

# -----------------------------------
# 5. Case-Insensitive Search
# -----------------------------------

word = "samsung"
pattern = rf"{re.escape(word)}"
search_products(pattern, "5. Case-Insensitive Search")

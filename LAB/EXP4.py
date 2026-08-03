def make_plural(noun):

    if noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"

    elif noun.endswith("y") and noun[-2] not in "aeiou":
        return noun[:-1] + "ies"

    else:
        return noun + "s"


word = input("Enter a noun: ")

print("Plural:", make_plural(word))

words = ["writes", "writing", "written"]

print("-"*110)
print("{:<12}{:<25}{:<15}{:<15}{:<15}".format(
    "Word","State Transition","Root","Pattern","Normalized"))
print("-"*110)

for word in words:

    if word == "writes":
        state = "Start -> write -> +s -> End"
        root = "write"
        pattern = "Regular"

    elif word == "writing":
        state = "Start -> write -> +ing -> End"
        root = "write"
        pattern = "Regular"

    elif word == "written":
        state = "Start -> write -> irregular(en) -> End"
        root = "write"
        pattern = "Irregular"

    print("{:<12}{:<25}{:<15}{:<15}{:<15}".format(
        word,state,root,pattern,root))

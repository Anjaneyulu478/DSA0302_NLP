def check_string(s):
    if s.endswith("ab"):
        print("Accepted")
    else:
        print("Rejected")

string = input("Enter a string: ")
check_string(string)

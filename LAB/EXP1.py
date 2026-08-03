import re

text = "My phone number is 9876543210 and my email is student@gmail.com"

# Search phone number
phone = re.search(r"\d{10}", text)

# Search email
email = re.search(r"\S+@\S+", text)

if phone:
    print("Phone Number:", phone.group())

if email:
    print("Email:", email.group())

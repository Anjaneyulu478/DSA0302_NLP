import re

# -----------------------------------
# Student Details
# -----------------------------------

student = {
    "Register Number": "23CS001",
    "Email": "rahul@university.edu",
    "Course Code": "CS301",
    "Semester": "5",
    "Mobile": "+91 9876543210"
}

# -----------------------------------
# Validation Functions
# -----------------------------------

def validate_register_number(reg_no):
    pattern = r"^\d{2}[A-Z]{2}\d{3}$"
    return re.fullmatch(pattern, reg_no)


def validate_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@university\.edu$"
    return re.fullmatch(pattern, email)


def validate_course_code(course):
    pattern = r"^[A-Z]{2}\d{3}$"
    return re.fullmatch(pattern, course)


def validate_semester(semester):
    pattern = r"^[1-8]$"
    return re.fullmatch(pattern, semester)


def validate_mobile(mobile):
    pattern = r"^(?:\+91\s?)?[6-9]\d{9}$"
    return re.fullmatch(pattern, mobile)

# -----------------------------------
# Validation Process
# -----------------------------------

status = True

print("=" * 60)
print("STUDENT REGISTRATION VALIDATION")
print("=" * 60)

# Register Number
if validate_register_number(student["Register Number"]):
    print("Register Number : Valid")
else:
    print("Register Number : Invalid")
    status = False

# Email
if validate_email(student["Email"]):
    print("Email           : Valid")
else:
    print("Email           : Invalid")
    status = False

# Course Code
if validate_course_code(student["Course Code"]):
    print("Course Code     : Valid")
else:
    print("Course Code     : Invalid")
    status = False

# Semester
if validate_semester(student["Semester"]):
    print("Semester        : Valid")
else:
    print("Semester        : Invalid")
    status = False

# Mobile
if validate_mobile(student["Mobile"]):
    print("Mobile Number   : Valid")
else:
    print("Mobile Number   : Invalid")
    status = False

# -----------------------------------
# Final Status Report
# -----------------------------------

print("\n" + "=" * 60)
print("REGISTRATION STATUS REPORT")
print("=" * 60)

if status:
    print("Registration Successful")
else:
    print("Registration Failed")

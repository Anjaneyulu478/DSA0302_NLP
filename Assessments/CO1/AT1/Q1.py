import re

# -----------------------------
# Sample Resume Dataset
# -----------------------------

resumes = [
"""
Name: John Smith
Email: john.smith@gmail.com
Phone: +91 9876543210

Skills:
Python, SQL, Machine Learning, NLP

Experience: 3 years as Software Engineer
""",

"""
Name: Alice Johnson
Email: alice123@yahoo.com
Phone: 9123456780

Skills:
Java, SQL

Experience: 1 year
""",

"""
Name: David Kumar
Email: david.kumar@company.com
Mobile: 9988776655

Skills:
Python, Java, SQL

Experience: 5 years
"""
]

# --------------------------------
# Technical Skills List
# --------------------------------

technical_skills = [
    "Python",
    "Java",
    "SQL",
    "Machine Learning",
    "NLP"
]

# --------------------------------
# Function to Extract Resume Details
# --------------------------------

def extract_resume_info(resume):

    # Name
    name_pattern = r"Name:\s*([A-Za-z ]+)"
    name = re.search(name_pattern, resume)

    # Email
    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    email = re.search(email_pattern, resume)

    # Phone Number
    phone_pattern = r"(?:\+91\s?)?[6-9]\d{9}"
    phone = re.search(phone_pattern, resume)

    # Experience
    experience_pattern = r"(\d+)\s+year"
    experience = re.search(experience_pattern, resume)

    # Skills
    found_skills = []

    for skill in technical_skills:
        if re.search(skill, resume, re.IGNORECASE):
            found_skills.append(skill)

    profile = {
        "Name": name.group(1) if name else "Not Found",
        "Email": email.group() if email else "Not Found",
        "Phone": phone.group() if phone else "Not Found",
        "Experience": int(experience.group(1)) if experience else 0,
        "Skills": found_skills
    }

    return profile

# --------------------------------
# Extract Information
# --------------------------------

profiles = []

for resume in resumes:
    info = extract_resume_info(resume)
    profiles.append(info)

# --------------------------------
# Display Structured Summary
# --------------------------------

print("=" * 60)
print("STRUCTURED CANDIDATE PROFILES")
print("=" * 60)

for candidate in profiles:

    print("\nName       :", candidate["Name"])
    print("Email      :", candidate["Email"])
    print("Phone      :", candidate["Phone"])
    print("Experience :", candidate["Experience"], "Years")
    print("Skills     :", ", ".join(candidate["Skills"]))

# --------------------------------
# Eligible Candidates
# --------------------------------

print("\n")
print("=" * 60)
print("ELIGIBLE CANDIDATES")
print("=" * 60)

for candidate in profiles:

    if candidate["Experience"] >= 2 and "Python" in candidate["Skills"]:
        print(candidate["Name"])

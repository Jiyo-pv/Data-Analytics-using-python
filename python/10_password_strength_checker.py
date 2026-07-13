# Q10 Password strength checker - @JIYO P V 2026-07-13
pwd = input("Enter password: ")
missing = []

if len(pwd) < 8:
    missing.append("At least 8 characters")

has_digit = False
has_upper = False
has_lower = False
has_special = False

specials = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

for c in pwd:
    if c.isdigit():
        has_digit = True
    elif c.isupper():
        has_upper = True
    elif c.islower():
        has_lower = True
    elif c in specials:
        has_special = True

if not has_digit:
    missing.append("At least one digit")
if not has_upper:
    missing.append("At least one uppercase")
if not has_lower:
    missing.append("At least one lowercase")
if not has_special:
    missing.append("At least one special character")

if not missing:
    print("Strong Password")
else:
    print("Weak Password")
    print("Missing:")
    for m in missing:
        print("-", m)

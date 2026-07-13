# Q01 Check valid variable name - @JIYO P V 2026-07-13
import keyword


name = input("Enter variable name: ").strip()

if name.isidentifier() and not keyword.iskeyword(name):
    print("Valid variable name")
else:
    print("Invalid variable name")

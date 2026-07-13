# Q03 Upper lower length reverse palindrome - @JIYO P V 2026-07-13
def process_string(text):
    print("Upper:", text.upper())
    print("Lower:", text.lower())
    print("Length:", len(text))
    print("Reverse:", text[::-1])
    if text == text[::-1]:
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")


process_string(input("Enter string: "))

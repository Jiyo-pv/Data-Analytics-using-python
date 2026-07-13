# Q20 Custom exception for invalid age - @JIYO P V 2026-07-13
class InvalidAgeException(Exception):
    pass


def check_age(age):
    if age < 18 or age > 60:
        raise InvalidAgeException("Age must be between 18 and 60")
    print("Valid age")


try:
    age = int(input("Enter age: "))
    check_age(age)
except InvalidAgeException as e:
    print("InvalidAgeException:", e)
except ValueError:
    print("Enter a valid integer")

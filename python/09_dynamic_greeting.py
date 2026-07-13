# Q09 Greeting with variable arguments - @JIYO P V 2026-07-13
def greet_people(*names):
    if len(names) == 0:
        print("Hello, stranger!")
    elif len(names) == 1:
        print("Hello, " + names[0] + "!")
    else:
        msg = "Hello, "
        i = 0
        while i < len(names):
            if i == len(names) - 1:
                msg += "and " + names[i]
            else:
                msg += names[i] + ", "
            i += 1
        msg += "!"
        print(msg)


greet_people()
greet_people("Alice")
greet_people("Bob", "Charlie")
greet_people("David", "Eve", "Frank")

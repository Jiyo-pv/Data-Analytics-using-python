# Q08 Even odd palindrome armstrong prime perfect - @JIYO P V 2026-07-13
def is_even(n):
    return n % 2 == 0


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


def is_armstrong(n):
    s = str(abs(n))
    p = len(s)
    total = 0
    for d in s:
        total += int(d) ** p
    return total == abs(n)


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def is_perfect(n):
    if n <= 1:
        return False
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return total == n


n = int(input("Enter number: "))
if is_even(n):
    print("Even")
else:
    print("Odd")

if is_palindrome(n):
    print("Palindrome: Yes")
else:
    print("Palindrome: No")

if is_armstrong(n):
    print("Armstrong: Yes")
else:
    print("Armstrong: No")

if is_prime(n):
    print("Prime: Yes")
else:
    print("Prime: No")

if is_perfect(n):
    print("Perfect: Yes")
else:
    print("Perfect: No")

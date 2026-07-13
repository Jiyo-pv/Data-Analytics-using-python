# Q11 Recursive sum and factorial - @JIYO P V 2026-07-13
def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


for n in [5, 10, 18]:
    print("n=", n, "sum=", recursive_sum(n), "factorial=", factorial(n))

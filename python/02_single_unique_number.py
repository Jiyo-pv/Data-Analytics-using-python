# Q02 Find single unique number - @JIYO P V 2026-07-13
nums = list(map(int, input("Enter numbers (space separated): ").split()))

result = 0
for n in nums:
    result ^= n

print("Unique number:", result)

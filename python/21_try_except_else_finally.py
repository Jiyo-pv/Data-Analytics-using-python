# Q21 Try except else finally flow - @JIYO P V 2026-07-13
balance = 5000

try:
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient balance")
except ValueError as e:
    print("Transaction failed:", e)
else:
    balance -= amount
    print("Transaction success")
    print("Remaining balance:", balance)
finally:
    print("Transaction ended")

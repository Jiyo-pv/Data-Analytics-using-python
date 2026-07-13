# Q22 Convert date format with exception handling - @JIYO P V 2026-07-13
from datetime import datetime


date_str = input("Enter date (dd-mm-yyyy): ").strip()

try:
    d = datetime.strptime(date_str, "%d-%m-%Y")
    print(d.strftime("%B %d, %Y"))
except ValueError:
    print("Invalid date format or invalid date")

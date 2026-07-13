# Q07 Conference attendees using sets - @JIYO P V 2026-07-13
a = set(input("AI & Data Science attendees (comma separated): ").split(","))
b = set(input("Cybersecurity attendees (comma separated): ").split(","))

clean_a = set()
for x in a:
	x = x.strip()
	if x != "":
		clean_a.add(x)

clean_b = set()
for x in b:
	x = x.strip()
	if x != "":
		clean_b.add(x)

a = clean_a
b = clean_b

print("All unique:", a | b)
print("Both sessions:", a & b)
print("Only AI & Data Science:", a - b)
print("Only Cybersecurity:", b - a)

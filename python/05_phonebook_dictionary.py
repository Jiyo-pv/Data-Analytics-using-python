# Q05 Phonebook using dictionary - @JIYO P V 2026-07-13
phonebook = {}

while True:
    print("\n1.Add/Update 2.Search 3.Delete 4.Display 5.Exit")
    ch = input("Choose: ").strip()

    if ch == "1":
        name = input("Name: ").strip()
        num = input("Number: ").strip()
        phonebook[name] = num
        print("Saved")
    elif ch == "2":
        name = input("Name to search: ").strip()
        print(phonebook.get(name, "Not found"))
    elif ch == "3":
        name = input("Name to delete: ").strip()
        print("Deleted" if phonebook.pop(name, None) else "Not found")
    elif ch == "4":
        print(phonebook)
    elif ch == "5":
        break
    else:
        print("Invalid choice")

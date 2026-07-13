# Q04 Menu driven string operations - @JIYO P V 2026-07-13
main = input("Enter main string: ")

while True:
    print("\n1.Substring check 2.Count character 3.Replace 4.Upper 5.Exit")
    ch = input("Choose: ").strip()

    if ch == "1":
        sub = input("Enter substring: ")
        print("Present" if sub in main else "Not present")
    elif ch == "2":
        c = input("Enter character: ")
        print("Count:", main.count(c))
    elif ch == "3":
        old = input("Old substring: ")
        new = input("New substring: ")
        main = main.replace(old, new)
        print("Updated:", main)
    elif ch == "4":
        print(main.upper())
    elif ch == "5":
        break
    else:
        print("Invalid choice")

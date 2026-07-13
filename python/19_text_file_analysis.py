# Q19 Read file and analyze words - @JIYO P V 2026-07-13
path = input("Enter .txt file path: ").strip()

try:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    lines = text.splitlines()
    words = text.split()
    chars = len(text)

    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", chars)

    freq = {}
    for w in words:
        word = w.lower().strip(".,!?;:\"'()[]{}")
        if word != "":
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print("Top 5 words:")
    i = 0
    for word, count in sorted_words:
        print(word, count)
        i += 1
        if i == 5:
            break
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")

# Q12 Main analyzer using modules - @JIYO P V 2026-07-13
from q12_text_preprocessor import normalize_text, tokenize_text
from q12_text_analyzer import word_frequency, character_count, unique_word_count


text = input("Enter text: ")
normalized = normalize_text(text)
tokens = tokenize_text(normalized)
freq = word_frequency(tokens)
chars = character_count(text)
unique = unique_word_count(tokens)

print("Original:", text)
print("Normalized:", normalized)
print("Tokens:", tokens)
print("Word Frequency:", freq)
print("Total Char Count:", chars)
print("Unique Word Count:", unique)

print("\nDocstrings:")
print(normalize_text.__doc__)
print(tokenize_text.__doc__)
print(word_frequency.__doc__)
print(character_count.__doc__)
print(unique_word_count.__doc__)

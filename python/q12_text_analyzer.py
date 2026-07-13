# Q12 Text analyzer module - @JIYO P V 2026-07-13
def word_frequency(word_list: list[str]) -> dict[str, int]:
    """Count occurrences of each word."""
    freq = {}
    for w in word_list:
        freq[w] = freq.get(w, 0) + 1
    return freq


def character_count(text: str) -> int:
    """Count alphabetic characters only."""
    count = 0
    for ch in text:
        if ch.isalpha():
            count += 1
    return count


def unique_word_count(word_list: list[str]) -> int:
    """Count unique words."""
    return len(set(word_list))

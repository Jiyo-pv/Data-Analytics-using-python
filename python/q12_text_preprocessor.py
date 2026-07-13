# Q12 Text preprocessor module - @JIYO P V 2026-07-13
def normalize_text(text: str) -> str:
    """Convert to lowercase and remove punctuation."""
    cleaned = ""
    for ch in text.lower():
        if ch.isalnum() or ch.isspace():
            cleaned += ch
    return cleaned


def tokenize_text(text: str) -> list[str]:
    """Split text into words."""
    return text.split()

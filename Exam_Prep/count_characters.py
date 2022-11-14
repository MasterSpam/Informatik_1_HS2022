def count_characters(text):
    all_chars = {}
    for char in text:
        if char not in all_chars:
            all_chars[char] = text.count(char)
    return all_chars


assert (count_characters("hello") == {"h": 1, "e": 1, "l": 2, "o": 1})
assert (count_characters("Прогресс") == {"П": 1, "р": 2, "о": 1, "г": 1, "е": 1, "с": 2})
assert (count_characters("<3") == {"<": 1, "3": 1})
assert (count_characters("") == {})

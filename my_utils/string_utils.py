"""
string_utils.py

This module has simple functions that work with strings (text).
"""


def reverse_string(text):
    """Return the given text reversed (back to front)."""
    return text[::-1]


def count_vowels(text):
    """Count and return how many vowels (a, e, i, o, u) are in the text."""
    vowels = "aeiouAEIOU"
    count = 0
    for letter in text:
        if letter in vowels:
            count = count + 1
    return count


def capitalize_words(text):
    """Return the text with the first letter of every word capitalized."""
    words = text.split()
    new_words = []
    for word in words:
        new_word = word.capitalize()
        new_words.append(new_word)
    result = " ".join(new_words)
    return result

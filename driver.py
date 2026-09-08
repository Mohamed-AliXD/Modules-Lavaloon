"""
driver.py

This script is NOT part of the package.
It is a separate file that imports and uses the my_utils package
to prove that the package works and can be reused.
"""

from my_utils.string_utils import reverse_string, count_vowels, capitalize_words
from my_utils.math_utils import add, subtract, multiply, divide


def main():
    """Run some simple examples using the my_utils package."""

    print("---- String Utils Examples ----")

    text = "hello world"
    print("Original text:", text)
    print("Reversed text:", reverse_string(text))
    print("Number of vowels:", count_vowels(text))
    print("Capitalized words:", capitalize_words(text))

    print("\n---- Math Utils Examples ----")

    a = 10
    b = 5
    print(a, "+", b, "=", add(a, b))
    print(a, "-", b, "=", subtract(a, b))
    print(a, "*", b, "=", multiply(a, b))
    print(a, "/", b, "=", divide(a, b))

    print("\n---- Divide by Zero Example ----")
    divide(10, 0)


if __name__ == "__main__":
    main()

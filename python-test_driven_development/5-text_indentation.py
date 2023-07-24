#!/usr/bin/python3
"""
Text indentation
"""


def text_indentation(text):
    """adds 2 lines after some characters"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    symbols = [".", "?", ":"]
    for i, char in text:
        if char in symbols:
            print(text[start:i + 1], end="\n\n")
            start = i + 1

    print(text[start:], end='')

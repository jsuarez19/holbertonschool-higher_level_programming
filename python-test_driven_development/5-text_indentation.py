#!/usr/bin/python3
"""
Text indentation
"""


def text_indentation(text):
    """adds 2 lines after some characters"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = " ".join(text.split())
    newText = ''
    symbols = [".", "?", ":"]
    for char in text:
        newText += char
        if char in symbols:
            newText = newText.strip()
            newText += "\n\n"

    newText = newText.replace(" \n", "\n")
    newText = newText.replace("\n ", "\n")
    print(newText, end='')

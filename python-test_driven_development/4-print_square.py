#!/usr/bin/python3
"""
Print square
"""


def print_square(size):
    """Iterates and print square"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print("")



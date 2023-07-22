#!/usr/bin/python3
"""
Integers addition
"""


def add_integer(a, b=98):
    """Adds two integers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    else:
        return result

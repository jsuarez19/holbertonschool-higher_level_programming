#!/usr/bin/python3
"""
My list
"""


class MyList(list):
    """Subclass of list"""
    def print_sorted(self):
        print(sorted(self))

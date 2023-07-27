#!/usr/bin/python3
"""
Only sub class of
"""


def inherits_from(obj, a_class):
    """object is an instance of a class that inherited?"""
    if (type(obj) == a_class):
        return False
    return issubclass(type(obj), a_class)

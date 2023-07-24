#!/usr/bin/python3
"""
Say my name
"""


def say_my_name(first_name, last_name=""):
    """Function that prints name"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    elif last_name != "":
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {} ".format(first_name))

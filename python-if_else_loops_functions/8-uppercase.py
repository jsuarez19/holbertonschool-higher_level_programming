#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 96 < ord(char) < 123:
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("{}".format(char), end="")

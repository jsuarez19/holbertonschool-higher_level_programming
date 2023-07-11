#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 64 < ord(char) < 91:
            print("{}", end="".format(chr(ord(char) + 32)))
        else:
            print("{}", end="".format(char))

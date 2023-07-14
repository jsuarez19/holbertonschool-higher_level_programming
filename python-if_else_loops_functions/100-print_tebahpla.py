#!/usr/bin/python3
i = 0
for char in "abcdefghijklmnopqrstuvwxyz"[::-1]:
    if i % 2 != 0:
        char = char.upper()
    print("{}".format(char), end="")
    i += 1

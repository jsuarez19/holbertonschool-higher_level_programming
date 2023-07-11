#!/usr/bin/python3
import sys
argc = len(sys.argv)
if argc == 1:
    print("0 arguments.")
elif argc != 1:
    print("{:d} argument".format(argc - 1), end="")
    if argc == 2:
        print("s", end="")
    print(":")
    for i in range(1, argc):
        print("{}: {}".format(i, sys.argv[i]))

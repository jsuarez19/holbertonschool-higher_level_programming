#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = -1
    for element in my_list:
        print("{:d}".format(my_list[i]))
        i = i - 1

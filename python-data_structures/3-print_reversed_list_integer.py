#!/usr/bin/python3
def print_list_integer(my_list=[]):
    i = 1
    for i, element in my_list:
        print("{:d}".format(my_list[-i]))

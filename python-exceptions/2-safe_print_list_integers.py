#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    aux = 0
    for element in my_list:
        try:
            print("{:d}".format(element), end='')
            aux += 1
        except (TypeError, ValueError):
            pass
    print()
    return aux

#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    aux = 0
    for i in array(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            aux += 1
        except (TypeError, ValueError):
            pass
    print()
    return aux
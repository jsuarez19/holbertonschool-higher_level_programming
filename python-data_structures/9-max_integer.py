#!/usr/bin/python3
def max_integer(my_list=[]):
    size = len my_list
    bigger = my_list[0]
    if size == 0:
        return None
    else:
        for element in my_list:
            if element > bigger:
                bigger = element
        return bigger

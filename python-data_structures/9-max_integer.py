#!/usr/bin/python3
def max_integer(my_list=[]):
    size = len(my_list)
    if size == 0:
        return None
    else:
    bigger = my_list[0]
        for element in my_list:
            if element > bigger:
                bigger = element
        return bigger

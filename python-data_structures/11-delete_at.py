#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    for i, x in my_list:
        if i != idx:
            new_list.append(x)
    return new_list

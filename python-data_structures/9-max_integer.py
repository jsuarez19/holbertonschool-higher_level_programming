#!/usr/bin/python3
if __name__ == '__main__':
    def max_integer(my_list=[]):
        size = len(my_list)
        bigger = 0
        if size == 0:
            return None
        else:
            for element in my_list:
                if element > bigger:
                    bigger = element
            return bigger

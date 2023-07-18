#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    aux = 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None:
        return result
    for i in range(len(roman_string) - 1, -1, -1):
        k = roman_string[i]
        v = dic[k]
        if v >= aux:
            result += v
        else:
            result = result - v
        aux = v

    return result

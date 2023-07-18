#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = 0
    biggestKey = None
    if a_dictionary is None:
        return biggestKey
    for k, v in a_dictionary.items():
        if v > biggest:
            biggest = v
            biggestKey = k
    return biggestKey

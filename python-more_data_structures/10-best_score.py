#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = 0
    biggestKey = None
    for k, v in a_dictionary.items():
        if v > biggest:
            biggest = v
            biggestKey = k
    return biggestKey

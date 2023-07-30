#!/usr/bin/python3
"""
From JSON string
"""


import json


def from_json_string(my_str):
    """returns object of a JSON"""
    json_obj = json.load(my_str)
    return json_obj

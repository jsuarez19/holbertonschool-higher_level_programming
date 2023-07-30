#!/usr/bin/python3
"""
Load, add, save
"""


import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
json_obj = load_from_json_file(filename)
json_obj.extend(sys.argv[1:])
save_to_json_file(json_obj, filename)

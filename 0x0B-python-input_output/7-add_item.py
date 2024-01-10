#!/usr/bin/python3
"""script that adds all arguments to a list, and then save them to a file"""


import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


list = list(sys.argv[1:])

try:
    od = load_from_json_file("add_item.json")
except Exception:
    od = []

od.extend(list)
save_to_json_file(od, "add_item.json")

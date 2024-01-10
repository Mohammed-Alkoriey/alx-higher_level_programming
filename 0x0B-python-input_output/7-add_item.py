#!/usr/bin/python3
"""script that adds all arguments to a list, and then save them to a file"""


import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    list = load_from_json_file('add_item.json')

    for x in range(1, sys.argc + 1):
        list.append(sys.argv[x])
    save_to_json_file(list, "add_item.json")

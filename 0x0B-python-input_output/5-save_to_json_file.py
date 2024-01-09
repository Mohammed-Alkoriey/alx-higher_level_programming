#!/usr/bin/python3
"""write an object to file using JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """object to JSON"""
    obj = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as f1:
        f1.write(obj)

#!/usr/bin/python3
"""write an object to file using JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """object to JSON"""
    with open(filename, "w", encoding="utf-8") as file1:
        json.dump(my_obj,file1)

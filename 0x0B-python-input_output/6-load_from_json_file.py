#!/usr/bin/python3
"""creates object from  a JSON file"""


import json


def load_from_json_file(filename):
    """the body of the function"""
    with open(filename, "w", encoding="utf-8") as file1:
        return(json.loads(file1))

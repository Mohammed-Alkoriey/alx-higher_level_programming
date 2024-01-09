#!/usr/bin/python3
"""return an object from  a JSON representation"""


import json


def from_json_string(my_str):
    """object to JSON"""
    obj = json.loads(my_str)
    return obj

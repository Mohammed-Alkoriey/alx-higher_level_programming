#!/usr/bin/python3
"""make a JSON representation of an object"""


import json


def to_json_string(my_obj):
    """object to JSON"""
    rep = json.dumps(my_obj)
    return rep

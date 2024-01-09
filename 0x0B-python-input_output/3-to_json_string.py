#!/usr/bin/python3
import json
"""make a JSON representation of an object"""


def to_json_string(my_obj):
    """object to JSON"""
    rep = json.dumps(my_obj)
    return rep

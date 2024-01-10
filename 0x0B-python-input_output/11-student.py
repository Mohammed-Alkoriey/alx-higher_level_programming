#!/usr/bin/python3

"""student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        lis = {}
        if isinstance(attrs, list):
            for attr in attrs:
                try:
                    if isinstance(attr, str):
                        lis[attr] = self.__dict__[attr]
                except KeyError:
                    pass
            return lis
        else:
            return self.__dict__

    def reload_from_json(self, json):
        self.__dict__.update(json)

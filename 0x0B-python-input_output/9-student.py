#!/usr/bin/python3

"""student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        firs_tname = self.first_name
        last_name = self.last_name
        age = self.age

    def to_json(self):
        return self.__dict__

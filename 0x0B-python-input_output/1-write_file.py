#!/usr/bin/python3

"""write a string into a file"""


def write_file(filename="", text=""):
    """writing into a file"""
    with open(filename, "w+", encoding="utf-8") as file1:
        return file1.write(text)

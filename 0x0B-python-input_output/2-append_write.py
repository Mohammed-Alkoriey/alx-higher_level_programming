#!/usr/bin/python3

"""append a string into a file"""


def write_file(filename="", text=""):
    """appending into a file"""
    with open(filename, "a+", encoding="utf-8") as file1:
        return file1.write(text)

#!/usr/bin/python3

"""write a string into a text"""


def write_file(filename="", text=""):
    """reading from a file"""
    with open(filename, "w+", encoding="utf-8") as file1:
        file1.write(text)

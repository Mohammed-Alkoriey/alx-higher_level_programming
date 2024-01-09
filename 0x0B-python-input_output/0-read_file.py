#!/usr/bin/python3

"""Read a file function"""
def read_file(filename=""):
    """reading from a file"""
    with open(filename, encoding="utf-8") as file1:
        print(file1.read(), end="")

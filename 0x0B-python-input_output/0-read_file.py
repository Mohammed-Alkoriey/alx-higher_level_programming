#!/usr/bin/python3


def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as file1:
        print(file1.read(), end="")

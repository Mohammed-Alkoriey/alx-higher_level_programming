#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file1:
        file_content = file1.read()

        print(file_content)

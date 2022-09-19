#!/usr/bin/python3
""" input output"""


def write_file(filename="", text=""):
    """write in text file"""
    with open(filename, 'w') as f:
        f.write(text)
    return len(text)

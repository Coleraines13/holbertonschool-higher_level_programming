#!/usr/bin/python3
""" input output"""


def number_of_line(filename=""):
    """write in text file"""
    with open(filename, 'w') as f:
        f.write(text)
        return len(text)

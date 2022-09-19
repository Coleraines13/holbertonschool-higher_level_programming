#!/usr/bin/python3
""" input output"""


def number_of_line(filename=""):
    """write in text file"""
    with open(filename, 'r') as f:
        i = 0
        for lines in f:
            i += 1
    return(i)

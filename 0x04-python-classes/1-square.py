#!/usr/bin/python3
"""raising exceptions for square"""


class Square:
    """created class Square"""
    def __init__(self, size=0):
        """added attributes to square"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

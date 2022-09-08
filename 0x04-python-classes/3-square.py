#!/usr/bin/python3
"""added method area"""


class Square:
    """created class square"""
    def __init__(self, size=0):
        """assign atrributes to square"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__self.__size
            return size * size

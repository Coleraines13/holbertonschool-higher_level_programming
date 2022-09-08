#!/usr/bin/python3
"""added method area"""



class Square:
    """created class square"""
    def __init__(self, size=0):
        """assign atrributes to square"""
        self.__size = size

    # Property
    @property
    def size(self):
        return self.__size

    # Setter modifies
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

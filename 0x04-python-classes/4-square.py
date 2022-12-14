#!/usr/bin/python3
"""added method area"""


class Square:
    """created class square"""
    def __init__(self, size=0):
        """assign atrributes to square"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

       def area(self):
           return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        if self.__size <= 0:
            print()
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end='')
                print()

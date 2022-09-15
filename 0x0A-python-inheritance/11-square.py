#!/usr/bin/python3
"""square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square data"""

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """method to calculate square description"""
        return self.__size * self.__size

    def __str__(self):
        """ magic method to print square"""
        return "[Square] {}/{}".format(self.__size, self.__size)

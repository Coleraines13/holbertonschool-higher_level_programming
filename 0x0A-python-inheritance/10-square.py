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
        """method to calculate area of the square"""
        return self.__size * self.__size

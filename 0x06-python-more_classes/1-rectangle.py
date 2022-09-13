#!/usr/bin/python3

"""
this will define a rectangle
"""


class Rectangle:
    """ 
    this instantiates the rectangle
    """

    def __intit__(self, width=0, height=0):
        self.width = width
        self.heigth = heigth

    @property
    def width(self):
        """
        this returns the width property of our rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

        @property
        def heigth(self):
            return self.height
        @heigth.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__heigth = value

         def area(self):
             return self.__width * self.__heigth

         def perimeter(self):
             if self.width == 0 or self.height == 0:
                 return 0
             else:
                 return ((2 * self.__width) + (2 * self.__height))

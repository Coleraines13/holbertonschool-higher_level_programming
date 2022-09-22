#!/usr/bin/python3
"""almost a circle"""
from models.base import Base


class Rectangle(Base):
    """made sub class of base called rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """attributes of rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.heigth

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def hieght(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.height = value

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.x = value

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """print rectangle"""
        for i in range(self.__y):
            print("\n", end='')
        for i in range(self.__height):
            for i in range(self.__x):
                print(" ", end='')
            for i in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """return rectangle info"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """add arguments"""
        attr = ['id', 'width', 'height', 'x', 'y']
        i = 0
        if args:
            for arg in args:
                setattr(self, attr[i], args[i])
                i += 1
        if kwargs:
            for arg in kwargs:
                setattr(self, arg, kwargs[arg])

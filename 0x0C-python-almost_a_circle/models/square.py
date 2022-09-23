#!/usr/bin/python3
"""almost a circle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """created a subclass of a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """adds attribute to square"""
        super().__init__(self, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """string override"""
        return "[Square] ({}) {}/{} _ {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """assign arguments to attributes"""
        attr = ['id', 'size', 'x', 'y']
        i = 0
        if args:
            for arg in args:
                setattr(self, attr[i], args[i])
                i += 1
        if kwargs:
            for arg in args:
                setattr(self, arg, kwargs[arg])

    def to_dictionary(self):
        """dictionary representation"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

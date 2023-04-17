#!/usr/bin/python3
from models.base import Base
"""inherits from base.py"""


class Rectangle(Base):
    """private instances"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        """properties and theit setters"""

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            """checking if width is int"""

            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def heigth(self, value):
            """checking for int"""

            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            """checkingfor int"""

            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            elif value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value
        
        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            """checking for int"""

            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            elif value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value

#!/usr/bin/python3
from models.base import Base
"""inherits from base.py"""


class Rectangle(Base):
    """private instances"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """iniialises rectangle
         Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
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
            """setting x coordinate"""

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
            """stting y cordinate for rectangle"""

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

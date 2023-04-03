#!/usr/bin/python3
"""a class that defines a rectangle"""


class Rectangle():
    """private instance"""

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    """defining a width property"""

    @property
    def width(self):
        return self.__width

    """property setter"""

    @width.setter
    def width(self, value):
        """checking if width is an integer and greater than 0"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """defining height property to retrieve it"""
    @property
    def height(self):
        return self.__height

    """height property setter"""
    @height.setter
    def height(self, value):
        """checkin if height is an integer and greater than 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

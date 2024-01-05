#!/usr/bin/python3
"""
    defines a rectangle
"""


class Rectangle:
    """Representing a rectangle"""
    def __init__(self, width=0, height=0):
        """initializing"""
        self.width = width
        self.height = height

    @property    
    def width(self):
        """getter for private instance"""
        return self.__width
    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height
    @height.setter
    def height(self, value):
        """setter for heght"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

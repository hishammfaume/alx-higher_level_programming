#!/usr/bin/python3
"""class defining sqaure"""


class Square:
    """defning the private insatance"""
    def __init__(self, size=0):
        self.__size = size

    """property"""
    @property
    def size(self):
        return self.__size
    """property setter"""
    
    @size.setter
    def size(self, value):
        """chcking for errors"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        """other errors"""

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

        """area method"""
    def area(self):
            return self.__size ** 2

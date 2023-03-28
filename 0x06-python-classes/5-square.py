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
    """my print instance method prints ####"""
    def my_print(self):
        if self.__size == 0:
            print()
            """rprinting hashes"""
        for i in range(self.__size):
            print("#" * self.__size)

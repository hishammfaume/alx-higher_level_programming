#!/usr/bin/python3
"""classof sqaures"""


class Square:
    """defning the private insatance"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
    """position property"""
    @property
    def position(self):
        return self.__position
    """position setter"""
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

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
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

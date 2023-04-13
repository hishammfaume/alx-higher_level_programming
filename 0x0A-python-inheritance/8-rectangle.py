#!/usr/bin/pyhton3
"""class inheritance"""


class BaseGeometry():
    """public instance"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validating the value"""

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


"""creating a new class"""


class Rectangle(BaseGeometry):
    """defining the rectanglr"""

    def __init__(self, width, height):
        """making height and width private"""

        self.__width = width
        self.__height = height
        """using an instance fron beasegeo class"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

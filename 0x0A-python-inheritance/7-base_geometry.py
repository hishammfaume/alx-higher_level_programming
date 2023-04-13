#!/usr/bin/python3
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

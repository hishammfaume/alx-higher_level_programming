#!/usr/bin/python3
"""returns True if the object is exactly an instance of class"""


def is_same_class(obj, a_class):
    """returns a boolean if its same class"""

    if isinstance(obj, a_class):
        """checks if its same class """

        return True
    else:
        """checks if not same class"""

        return False

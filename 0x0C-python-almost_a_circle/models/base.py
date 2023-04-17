#!/usr/bin/python3
"""creaing a base class"""


class Base():
    """private attribute"""

    __nb_objects = 0

    """class constructor"""

    def __init__(self, id=None):
        """checking if id is one"""

        if id is not None:
            self.id = id
        else:
            """incrementing the number od objects"""

            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

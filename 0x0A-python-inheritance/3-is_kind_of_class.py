#!/usr/bin/python3
"""returns true if objectnis instance of"""


def is_kind_of_class(obj, a_class):
    """checking if its an instance of an obj"""

    if isinstance(obj, a_class):
        """returning a boolean"""

        return True
    else:
        return False

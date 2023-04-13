#!/usr/bin/python3
"""checks if an obk=j is inherited"""


def inherits_from(obj, a_class):
    """checking the inheritance"""

    if isinstance(obj, a_class):
        return True
    else:
        return False

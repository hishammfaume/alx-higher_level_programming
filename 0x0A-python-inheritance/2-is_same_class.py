#!/usr/bin/python3
"""returns True if the object is exactly an instance of class"""

def is_same_class(obj, a_class):
    """checking instance"""

    if isinstance(obj, a_class):
        return True
    else:
        return False

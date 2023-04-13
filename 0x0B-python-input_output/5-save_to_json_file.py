#!/usr/bin/python3
"""writes an Object to a text file,using a JSON"""
import json


def save_to_json_file(my_obj, filename):
    """passing obj to file"""

    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)

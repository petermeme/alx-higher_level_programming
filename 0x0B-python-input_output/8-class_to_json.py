#!/usr/bin/python3
"""
class to json module
"""


def class_to_json(obj):
    """function that returns the dictionary
    description with simple data structure"""

    return obj.__dict__

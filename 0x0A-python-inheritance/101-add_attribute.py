#!/usr/bin/python3
"""
=============================
Module with add_attribute
=============================
"""


def add_attribute(obj, objname, value):
    """add attribute to object
    args:
        obj: class object
        objname: object name
        value: value of attribute
    return
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, objname, value)

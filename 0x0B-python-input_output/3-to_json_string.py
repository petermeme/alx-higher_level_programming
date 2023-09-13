#!/usr/bin/python3
"""
Json_string module
"""


import json


def to_json_string(my_obj):
    """function that returns he JSON representation of an object(string)"""
    return json.dumps(my_obj)

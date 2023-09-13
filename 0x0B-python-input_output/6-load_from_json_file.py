#!/usr/bin/python3
"""
create an object module
"""


import json


def load_from_json_file(filename):
    """function that creates an Object from JSON file"""

    with open(filename) as f:
        return json.loads(f.read())

#!/usr/bin/python3
"""
MyList that inherits from list:
"""


class MyList(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
        """sorts a list"""

        print(sorted(list(self)))

#!/usr/bin/python3
"""Defines a class MagicClass"""
import math


class MagicClass:
    """
    MagicClass: defining class
    """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """area: returns area"""
        return self.__radius**2 * math.pi

    def circumference(self):
        """circumference: returns circum"""
        return 2 * math.pi * self.__radius

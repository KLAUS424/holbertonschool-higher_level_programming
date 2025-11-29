#!/usr/bin/python3
"""
6-base_geometry: Contains the BaseGeometry class with an unimplemented area() method.
"""


class BaseGeometry:
    """
    A base class for geometry-related objects, containing an unimplemented
    area calculation method.
    """

    def area(self):
        """
        Public instance method that raises an Exception indicating
        that the area calculation is not yet implemented in subclasses.

        Raises:
            Exception: Always raises an Exception with the message
                       "area() is not implemented".
        """
        raise Exception("area() is not implemented")

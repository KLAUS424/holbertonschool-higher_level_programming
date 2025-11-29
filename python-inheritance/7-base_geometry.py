#!/usr/bin/python3
"""
7-base_geometry: Contains the BaseGeometry class with area() and
integer_validator() methods.
"""


class BaseGeometry:
    """
    A base class for geometry-related objects, providing common validation
    and structure.
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

    def integer_validator(self, name, value):
        """
        Public instance method to validate that a value is a positive integer.

        Args:
            name (str): The name of the value (assumed to be a string).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

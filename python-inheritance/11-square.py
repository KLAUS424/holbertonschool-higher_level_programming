#!/usr/bin/python3
"""
Module 11-square.py
Contains the class Square that inherits from Rectangle (9-rectangle.py).

This version overrides the __str__ method to provide the square-specific
string representation: [Square] <size>/<size>.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, inheriting from Rectangle.
    The square is defined by a single side length 'size', which is validated
    and used as both the width and height of the underlying Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
         size (int): The side length of the square. Must be a positive integer.
        """

        self.integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)

    def __str__(self):
        """
        Returns the square's description in the format: [Square] <width>/<height>.
        Since width and height are equal to __size, we use that value.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

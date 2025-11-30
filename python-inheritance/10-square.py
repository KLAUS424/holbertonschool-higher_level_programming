#!/usr/bin/python3
"""
Module 10-square.py
Contains the class Square that inherits
 from Rectangle (9-rectangle.py).
The Square class must validate its size
using BaseGeometry's integer_validator.
"""

# Import the Rectangle class from the previous file
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Represents a square, inheriting properties and
    methods from Rectangle.
    A square is instantiated with a single
    size argument which is passed
    to the Rectangle constructor as both width and height.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The side length of the square.
              Must be a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

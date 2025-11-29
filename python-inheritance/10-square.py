#!/usr/bin/python3
"""
Module 10-square.py
Contains the class Square that inherits from Rectangle (9-rectangle.py).
The Square class must validate its size using BaseGeometry's integer_validator.
"""

# Import the Rectangle class from the previous file
# It is assumed that 9-rectangle.py exists and properly imports BaseGeometry.
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Represents a square, inheriting properties and methods from Rectangle.
    A square is instantiated with a single size argument which is passed
    to the Rectangle constructor as both width and height.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The side length of the square. Must be a positive integer.
        """
        # 1. Validate 'size' using the inherited integer_validator method
        # which checks if size is an integer and greater than 0.
        self.integer_validator("size", size)
        # 2. Call the parent class (Rectangle) constructor.
        # Since a square has equal sides, size is passed for both width and height.
        super().__init__(size, size)
        # 3. Store 'size' as a private instance attribute __size
        self.__size = size
        # Note on methods:
        # - area(): Inherited from Rectangle, which correctly calculates size * size.
        # - __str__(): Inherited from Rectangle, which outputs [Rectangle] size/size.

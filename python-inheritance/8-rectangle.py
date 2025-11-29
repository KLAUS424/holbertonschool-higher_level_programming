#!/usr/bin/python3
"""
8-rectangle: Contains the Rectangle class which inherits from BaseGeometry.
"""

# Import the parent class BaseGeometry from the previous file
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle, inheriting validation logic from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        The width and height are validated using integer_validator 
        and stored as private instance attributes.
        """
        # Validate and set width (private attribute)
        self.integer_validator("width", width)
        self.__width = width

        # Validate and set height (private attribute)
        self.integer_validator("height", height)
        self.__height = height

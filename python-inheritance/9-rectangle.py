#!/usr/bin/python3
"""Rectangle module, inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize rectangle with width and height"""
        # Validate width and height using BaseGeometry method
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        # Private attributes
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

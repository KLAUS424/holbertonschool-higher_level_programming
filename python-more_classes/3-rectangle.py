#!/usr/bin/python3
"""
3-rectangle: Module that defines a Rectangle class.

This module provides the Rectangle class, which is defined by private
instance attributes 'width' and 'height'. It includes properties for
validation, methods for calculation (area/perimeter), and string
representation methods (__str__ and __repr__).
"""


class Rectangle:
    """
    Represents a rectangle figure.

    Manages the size of the rectangle through validated width and height
    properties and provides methods for calculation and representation.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        The initializer uses the setters to validate the initial values.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        # The constructor calls the setters for validation
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method to retrieve the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method to set the width of the rectangle with validation.

        Args:
            value (int): The new width for the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter method to retrieve the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method to set the height of the rectangle with validation.

        Args:
            value (int): The new height for the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle (width * height).

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Perimeter is calculated as 2 * (width + height).
        If width or height is 0, the perimeter is 0.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns the printable string representation of the Rectangle instance.

        The rectangle is represented by the character '#'.
        If width or height is 0, returns an empty string.

        Returns:
            str: String representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        # Hər sətir üçün genişlik qədər '#' təkrarlanır
        line = "#" * self.__width

        # Hündürlük qədər sətirləri birləşdirir
        # Hər sətir yeni sətir xarakteri ilə ayrılır, lakin sonda yeni sətir olmur
        return '\n'.join([line for i in range(self.__height)])

    def __repr__(self):
        """
        Returns the official string representation of the Rectangle instance.

        The string can be used to recreate the object using eval().

        Returns:
            str: String representation: "Rectangle(width, height)"
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

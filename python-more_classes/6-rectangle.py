#!/usr/bin/python3
"""
6-rectangle: Module that defines a Rectangle class with an instance counter.

This module introduces a public class attribute `number_of_instances`
to track the creation and deletion of Rectangle objects.
"""


class Rectangle:
    """
    Represents a rectangle figure and tracks the number of instances.

    Public class attribute:
        number_of_instances (int): Tracks the total count of active Rectangle instances.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Increments the `number_of_instances` class attribute upon creation.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        # Increment the counter for every new instance created
        Rectangle.number_of_instances += 1

        # Initialize instance attributes (using setters for validation)
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

        # Construct the representation line by line
        line = "#" * self.__width
        
        # Join lines with newline character, ensuring no trailing newline
        return '\n'.join([line for i in range(self.__height)])

    def __repr__(self):
        """
        Returns the official string representation of the Rectangle instance,
        allowing recreation of the object using eval().

        Returns:
            str: String representation: "Rectangle(width, height)"
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor method called when an instance of Rectangle is garbage
        collected (deleted).

        Prints the required deletion message and decrements the
        `number_of_instances` class attribute.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

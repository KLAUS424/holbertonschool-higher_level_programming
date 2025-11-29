#!/usr/bin/python3
"""
9-rectangle: Module that defines a Rectangle class.

This version introduces a class method `square` for creating square instances
and retains instance tracking, property validation, area/perimeter calculation,
and the static comparison method.
"""


class Rectangle:
    """
    Represents a rectangle figure and tracks the number of instances.

    Public class attributes:
        number_of_instances (int): Tracks the total count of active Rectangle
            instances.
        print_symbol (any): The symbol/value used for the string
            representation of the rectangle. Initialized to '#'.
    """
    number_of_instances = 0
    print_symbol = "#"

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two Rectangles and returns the one with the larger area.

        Args:
            rect_1 (Rectangle): The first rectangle instance to compare.
            rect_2 (Rectangle): The second rectangle instance to compare.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance
                of Rectangle.

        Returns:
            Rectangle: rect_1 if its area is greater than or equal to
                rect_2's area, otherwise returns rect_2.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size.

        Args:
            cls: The class itself (Rectangle).
            size (int, optional): The side length of the square. Defaults to 0.

        Returns:
            Rectangle: A new instance of Rectangle where width == height
                == size.
        """
        return cls(size, size)

    def __str__(self):
        """
        Returns the printable string representation of the Rectangle instance.

        The rectangle is represented by the character(s) stored in
        `print_symbol`.
        If width or height is 0, returns an empty string.

        Returns:
            str: String representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        # Use instance-specific print_symbol if set, otherwise use class symbol
        symbol = str(self.print_symbol)

        # Construct one line of the rectangle
        line = symbol * self.__width

        # Join lines with newline character
        return '\n'.join([line for i in range(self.__height)])

    def __repr__(self):
        """
        Returns the official string representation of the Rectangle,
        allowing object recreation using eval().

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

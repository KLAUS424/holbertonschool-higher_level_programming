#!/usr/bin/python3
"""
1-my_list: Contains the MyList class that inherits from the built-in list.
"""


class MyList(list):
    """
    A class that inherits from 'list' and adds a public instance method
    to print the list elements sorted in ascending order.

    All elements are assumed to be of type int.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending sorted order.

        Note: The original list (self) is NOT modified. It uses the
              built-in sorted() function to return a new sorted list,
              which is then printed.
        """
        print(sorted(self))

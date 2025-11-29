#!/usr/bin/python3
"""
2-is_same_class: Contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class, 
              otherwise False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False

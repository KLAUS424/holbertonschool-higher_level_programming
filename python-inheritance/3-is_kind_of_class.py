#!/usr/bin/python3
"""
3-is_kind_of_class: Contains the function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of the specified class or
    if the object is an instance of a class that inherited from the
    specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class or type to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass,
              otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

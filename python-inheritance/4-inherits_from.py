#!/usr/bin/python3
"""
4-inherits_from: Contains the function inherits_from
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The base class to compare against.

    Returns:
        bool: True if obj's class is a subclass of a_class, but not
              a_class itself; otherwise False.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False

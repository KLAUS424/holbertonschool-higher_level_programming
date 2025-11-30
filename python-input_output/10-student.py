#!/usr/bin/python3
"""
Module 10-student
Contains the updated Student class definition
 with selective JSON serialization.
"""


class Student:
    """
    Defines a student with public instance attributes:
      first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        # Public instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list, optional):
              A list of strings specifying attribute names
              to retrieve. If None or not a list of strings,
              all attributes are retrieved. Defaults to None.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):

            return {
                key: self.__dict__[key]
                for key in attrs if key in self.__dict__
            }
        return self.__dict__

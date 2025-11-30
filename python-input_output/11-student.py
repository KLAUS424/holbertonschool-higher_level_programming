#!/usr/bin/python3
"""
Module 11-student
Contains the Student class definition,
  implementing serialization (to_json)
and deserialization (reload_from_json).
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

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.

        The method iterates through the key-value pairs of
         the input dictionary
        and sets the corresponding public instance attributes.

        Args:
            json (dict): A dictionary where keys are attribute names (str)
                         and values are the new attribute values.
        """

        for key, value in json.items():

            setattr(self, key, value)

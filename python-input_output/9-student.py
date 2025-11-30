#!/usr/bin/python3
"""
Module 9-student
Contains the Student class definition.
"""


class Student:
    """
    Defines a student with public instance attributes: first_name, last_name, and age.
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

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.
        The dictionary contains all attributes of the instance.

        Returns:
            dict: A dictionary containing the student's attributes.
        """

        return self.__dict__

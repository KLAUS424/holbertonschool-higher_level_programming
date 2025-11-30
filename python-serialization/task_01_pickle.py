#!/usr/bin/env python3
"""
Module task_01_pickle
Provides a CustomObject class with serialization and deserialization
methods using the 'pickle' module.
"""
import pickle
import os


class CustomObject:
    """
    A custom class with attributes and methods for serialization
    and deserialization using pickle.
    """
    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the object's attributes in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance of the object using pickle and
        saves it to the provided filename.

        Args:
            filename (str): The filename for the output pickle file.

        Returns:
            bool: True on success, False on failure.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            return True
        except IOError as e:
            print(f"Serialization Error: Failed to write to file {filename}. Error: {e}")
            return False
        except pickle.PicklingError as e:
            print(f"Serialization Error: Failed to pickle object. Error: {e}")
            return False
        except Exception as e:
            print(f"An unexpected error occurred during serialization: {e}")
            return False

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and deserializes an instance of CustomObject from the provided
        filename using pickle.

        Args:
            filename (str): The filename of the input pickle file.

        Returns:
            CustomObject or None: An instance of CustomObject on success,
                                  None on failure (e.g., file not found or malformed).
        """
        try:

            with open(filename, 'rb') as f:

                return pickle.load(f)
        except FileNotFoundError:
            print(f"Deserialization Error: File not found at {filename}.")
            return None
        except pickle.UnpicklingError as e:

            print(f"Deserialization Error: Failed to unpickle data from {filename}. Error: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred during deserialization: {e}")
            return None


if __name__ == '__main__':

    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()


    print("\nSerializing object to object.pkl...")
    success = obj.serialize("object.pkl")

    if success:

        new_obj = CustomObject.deserialize("object.pkl")
        if new_obj:
            print("\nDeserialized Object:")
            new_obj.display()
            print("\nCheck identity (should be False):", obj is new_obj)

        print("\nTesting invalid file path for deserialization:")
        non_existent_obj = CustomObject.deserialize("non_existent_file.pkl")
        print(f"Result for non-existent file: {non_existent_obj}")

        try:
            os.remove("object.pkl")
        except OSError:
            pass

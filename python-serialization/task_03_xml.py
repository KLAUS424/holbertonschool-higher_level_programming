#!/usr/bin/env python3
"""
Module task_03_xml
Provides functions for serializing Python dictionaries to XML
and deserializing XML back into dictionaries using xml.etree.ElementTree.
"""
import xml.etree.ElementTree as ET
import os


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML format and saves it to a file.
    The XML structure will be:
    <root_tag>
        <key1>value1</key1>
        <key2>value2</key2>
        ...
    </root_tag>

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the output XML file.

    Returns:
        bool: True on success, False on failure.
    """
    if not isinstance(dictionary, dict):
        print("Error: Input must be a dictionary.")
        return False
    try:

        root = ET.Element("data")


        for key, value in dictionary.items():
            child = ET.SubElement(root, key)

            child.text = str(value)

        tree = ET.ElementTree(root)

        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True

    except Exception as e:
        print(f"Serialization Error: Failed to write XML to {filename}. Error: {e}")
        return False


def deserialize_from_xml(filename):
    """
    Reads XML data from a file and returns a deserialized Python dictionary.

    Args:
        filename (str): The name of the input XML file.

    Returns:
        dict or None: The reconstructed Python dictionary on success,
                      None on failure (e.g., file not found or parsing error).
    """
    reconstructed_dict = {}
    try:

        tree = ET.parse(filename)
        root = tree.getroot()


        for child in root:

            reconstructed_dict[child.tag] = child.text
        return reconstructed_dict

    except FileNotFoundError:
        print(f"Deserialization Error: File not found at {filename}.")
        return None
    except ET.ParseError as e:
        print(f"Deserialization Error: Failed to parse XML from {filename}. Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during XML deserialization: {e}")
        return None


if __name__ == "__main__":

    sample_dict = {
        'name': 'John',
        'age': 28,
        'city': 'New York',
        'is_active': True
     }

    xml_file = "data.xml"
    print("Original Dictionary:")
    print(sample_dict)

    if serialize_to_xml(sample_dict, xml_file):
        print(f"\nDictionary successfully serialized to {xml_file}")
    else:
        print("\nSerialization failed.")

    print("\nAttempting to deserialize data...")
    deserialized_data = deserialize_from_xml(xml_file)
    if deserialized_data is not None:
        print("\nDeserialized Data:")
        print(deserialized_data)

        print("\nNote: All values in the deserialized dictionary are strings.")
    print("\nTesting deserialization with non-existent file:")
    non_existent_data = deserialize_from_xml("non_existent_data.xml")
    print(f"Result for non-existent file: {non_existent_data}")


    try:
        if os.path.exists(xml_file):
            os.remove(xml_file)
    except OSError:
        pass

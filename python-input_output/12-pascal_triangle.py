#!/usr/bin/python3
"""
Module 12-pascal_triangle
Contains a function to generate Pascal's triangle up to n rows.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n.

    Args:
        n (int): The number of rows of the triangle to generate.

    Returns:
        list: A list of lists of integers representing the triangle, or
              an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):

        current_row = []

        current_row.append(1)

        if i > 0:

            previous_row = triangle[i - 1]

            for j in range(1, len(previous_row)):
                element = previous_row[j - 1] + previous_row[j]
                current_row.append(element)


            current_row.append(1)

        triangle.append(current_row)

    return triangle

#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    max_value = my_list[0]
    for i in range(1, len(my_list)):
        current_element = my_list[i]
        if current_element > max_value:
            max_value = current_element
    return max_value

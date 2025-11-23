#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    n = len(roman_string)
    for i in range(n):
        current_val = roman_map.get(roman_string[i], 0)
        if i < n - 1:
            next_val = roman_map.get(roman_string[i+1], 0)
        else:
            next_val = 0
        if current_val < next_val:
            total -= current_val
        else:
            total += current_val
    return total

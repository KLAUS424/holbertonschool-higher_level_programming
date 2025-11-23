#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    def get_first_two(t):
        if len(t) >= 2:
            return (t[0], t[1])
        elif len(t) == 1:
            return (t[0], 0)
        else: 
            return (0, 0)
    a1, a2 = get_first_two(tuple_a)
    b1, b2 = get_first_two(tuple_b)
    first_sum = a1 + b1
    second_sum = a2 + b2
    return (first_sum, second_sum)

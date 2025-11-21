#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
if __name__ == "__main__":
    sum_result = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, sum_result))

    sub_result = sub(a, b)
    print("{:d} - {:d} = {:d}".format(a, b, sub_result))

    mul_result = mul(a, b)
    print("{:d} * {:d} = {:d}".format(a, b, mul_result))

    div_result = div(a, b)
    print("{:d} / {:d} = {:d}".format(a, b, div_result))

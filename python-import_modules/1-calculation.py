#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
if __name__ == "__main__":
   sum = add(a, b)
   print("{:d} + {:d} = {:d}".format(a, b, sum))
   sub = sub(a, b)
   print("{:d} - {:d} = {:d}".format(a, b, sub))
   mul = mul(a, b)
   print("{:d} * {:d} = {:d}".format(a, b, mul))
   div = mul(a, b)
   print("{:d} / {:d} = {:d}".format(a, b, div))

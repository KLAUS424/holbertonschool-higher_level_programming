#!/usr/bin/python3
import calculator_1
a = 10
b = 5
if __name__ == "__main__":
   sum = calculator_1.add(a, b)
   print("{:d} + {:d} = {:d}".format(a, b, sum))
   sub = calculator_1.sub(a, b)
   print("{:d} - {:d} = {:d}".format(a, b, sub))
   mul = calculator_1.mul(a, b)
   print("{:d} * {:d} = {:d}".format(a, b, mul))
   div = calculator_1.mul(a, b)
   print("{:d} / {:d} = {:d}".format(a, b, div))

#!/usr/bin/python3
import sys

if __name__ == "__main__":

    total_sum = 0

    for i in range(1, len(sys.argv)):

        argument_as_int = int(sys.argv[i])
        total_sum += argument_as_int

    print(total_sum)

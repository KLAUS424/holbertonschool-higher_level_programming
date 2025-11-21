#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1

    if num_args == 0:
        word = "arguments"
        punctuation = "."
    elif num_args == 1:
        word = "argument"
        punctuation = ":"
    else:
        word = "arguments"
        punctuation = ":"
    print("{:d} {}{}".format(num_args, word, punctuation))

    if num_args > 0:
        for i in range(1, len(sys.argv)):

            position = i
            argument_value = sys.argv[i]
            print("{:d}: {}".format(position, argument_value))

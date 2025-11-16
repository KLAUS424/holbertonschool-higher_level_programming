#!/usr/bin/python3
result = ""
for i in range(ord('a'), ord('z') + 1):
    char = chr(i)
    if char != 'q' and char != 'e':
        result += char
print("{}".format(result), end="")

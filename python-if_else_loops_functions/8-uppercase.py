#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        char_ord = ord(char)
        if ord('a') <= char_ord <= ord('z'):
            upper_char_ord = char_ord - (ord('a') - ord('A'))
            result += chr(upper_char_ord)
        else:
            result += char
    print("{}".format(result))

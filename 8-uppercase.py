#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if i >= 'a' and i <= 'z':
            charUpper = chr(ord(i) - 32)
            result += charUpper
        else:
            result += i
    print(result)
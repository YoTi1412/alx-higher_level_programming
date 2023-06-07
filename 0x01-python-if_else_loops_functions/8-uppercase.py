#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print("{}".format(chr(ord(char) - 32)) if char >= 'a' and char <= 'z'
              else "{}".format(char), end="")
    print("")

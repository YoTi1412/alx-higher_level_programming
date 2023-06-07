#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i)) if not i % 2
          else "{}".format(chr(i - 32)), end="")

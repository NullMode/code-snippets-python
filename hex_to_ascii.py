#!/usr/bin/python
import sys

if len(sys.argv) == 1:
    print "./script <hex>"
    sys.exit(1)


first = True
for arg in sys.argv:
        if first:
                first = False
        else:
                print arg + ' -> ' + arg.decode('hex')
#!/usr/bin/python
import sys

if len(sys.argv) == 1:
    print "[*] Usage: <length of number output>"
    print "    Example: length of 2 goes from 00 to 99"
    print "             length of 3 goes from 000 to 999"
    sys.exit(1)

length = int(sys.argv[1])
the_range = int("9" * length) + 1
list_of_numbers = [i for i in xrange(the_range)]
for i in list_of_numbers:
    if len(str(i)) < length + 1:
        current_length = len(str(i))
        padding_required = length - current_length
        print (padding_required * "0") + str(i)
else:
    print i

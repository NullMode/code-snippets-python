#!/usr/bin/python
import sys
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

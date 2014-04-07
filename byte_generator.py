# Generate a list of bytes, useful for checking for "bad bytes"
import sys
l = [i for i in range(10)]
l.extend(['a', 'b', 'c', 'd', 'e', 'f'])
r = l
 
for x in l:
        for y in r:
                sys.stdout.write('\\x' + str(x) + str(y))


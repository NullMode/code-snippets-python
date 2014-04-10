#!/usr/bin/python
import sys

if sys.argv == 1:
    print "[*] Usage: ./script <input file> <output file>"
    sys.exit(1)

filein = open(sys.argv[1], "r")
fileout = open(sys.argv[2], "w")

filein_list = []
for i in filein:
    filein_list.append(i.strip())
filein.close()

filein_list2 = filein_list

for i in filein_list:
        for j in filein_list2:
                fileout.write(i + j)
fileout.close()
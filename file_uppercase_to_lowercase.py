#!/usr/bin/python
import sys

if len(sys.argv) != 3:
    print "[*} Usage: ./script <input file> <output file>"

file1 = open(sys.argv[1], "r")
file2 = open(sys.argv[2], "w")

for i in file1:
        file2.write(i.lower())

file1.close()
file2.close()

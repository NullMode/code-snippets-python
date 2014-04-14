#!/usr/bin/python
from sys import argv
from sys import exit

if len(argv) != 3:
    print "[*] Usage ./script.py <file1> <file2>"
    print "See lines in file1 do not exist in file2."
    exit(1)

file1 = argv[1]
file2 = argv[2]

with open(file1, 'r') as f1:
    lines1 = f1.read().splitlines()

with open(file2, 'r') as f2:
    lines2 = f2.read().splitlines()

for f1 in lines1:
    if f1 not in lines2:
        print f1
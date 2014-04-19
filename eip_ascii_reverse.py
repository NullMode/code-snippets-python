#!/usr/bin/python
# Author: NullMode
# Description: Takes overwritten EIP value, changes to ASCII, reverses it, spits it out (doesn't swallow)

from sys import argv, exit, stdout


def usage():
    print "[!] ./eipoffset.py <EIP VALUE>"
    print "This function will take the EIP value, convert it to ASCII, then reverse it."


def err(msg):
    print "[!] " + msg

try:
    script, eip = argv
except ValueError:
    usage()
    exit(1)

if len(eip) != 8:
    err("EIP wrong length, check your input value.")
    exit(1)


try:
    eip = eip.decode("hex")
except TypeError:
    err("Error converting, check the value to make sure it's hex.")
    exit(1)

eip_list = [i for i in eip]

eip_list.reverse()

for i in eip_list:
    stdout.write(i)

print
exit(0)

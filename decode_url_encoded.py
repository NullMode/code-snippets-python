#!/usr/bin/python
from os.path import isfile
from sys import argv, exit

from urllib import unquote

if len(argv) < 3:
    print "[!] Usage: ./decode_url_encoded.py <input file> <output file>"
    exit(1)
else:
    input_file = argv[1]
    output_file = argv[2]
    output_file_exists = False

    if not isfile(input_file):
        print "[!] " + input_file + " does not exit!"
        exit(1)
    elif input_file is output_file:
        print "[!] The input file cannot be same as the output file!"
        exit(1)
    elif isfile(output_file):
        output_file_exists = True
        print "[!] Output file " + output_file + " already exists, overwrite?"
        while True:
            yes_no = raw_input("Y/N? ")
            if yes_no is 'Y':
                break
            elif yes_no is 'N':
                exit(0)

    output_file_handle = open(output_file, 'w')

    with open(input_file, 'r') as f:
        output_file_handle.write(unquote(f.read()))
    output_file_handle.close()

    if output_file_exists:
        print "[!] " + output_file + " has been overwritten!"

    print "[*] Decoding completed!"





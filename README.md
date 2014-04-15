About
=====

This repository is a collection of code snippets in python that might be useful for others. Below are explanations and examples for some of the scripts.

### ascii\_to\_hex.py
This script simply converts input ASCII to hex. Example:

	./script hello
	hello -> 68656c6c6f

### backup_class.py
A rough class that can be used to backup folders to a target folder.


### byte_generator.py
This is a simple snippet that outputs a list of all possible bytes. May be useful for scripting checks for bad bytes in shell code. Here's the output if you wanted a quick copy paste:

	\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff

### file\_lowercase\_to_uppercase.py
Converts an input file from lower case to upper case. Output is written to a user supplied file.

### file\_uppercase\_to_lowercase.py
Converts an input file from upper case to lower case. Output is written to a user supplied file.

### for\_each\_word\_in\_file\_add\_each\_word\_in\_file.py
This script is better explain with some pseudo code:

	for each line in the file:
		var1 = current line
		
		for each line in the file again:
			var2 = current line from this loop

			write to file: var1 + var2

Here is some output from the script running for more explanation:

	cat test.txt
	a
	b
	c

	python for_each_word_in_file_add_each_word_in_file.py test.txt test2.txt

	cat test2.txt
	aa
	ab
	ac
	ba
	bb
	bc
	ca
	cb
	cc

### generate\_padded\_number_list.py
This script takes in an integer value and generates a sequential number list. The input integer helps define the maximum number. If the application is given "2" as an argument, the application will return 00 to 99. If "4" is used, 0000 to 9999 is outputted. The key part of the script is to pad the numbers with 0's to equal the length of the input value.

    python generate\_padded\_number_list.py 4
	0000
	0001
	0002
	0003
	0004
	0005
	0006
	0007
	...


### hex\_to\_ascii.py
This script simply converts input hex to ASCII. Example:

	./script 68656c6c6f
	68656c6c6f -> help

### lines\_not\_in\_file.py
This script takes two files, a check is made to see what lines in file2 do not appear in file1. Below is an example

	cat file1
	a
	b
	c
	d
	e
	f
	
	cat file2
	d
	e
	f
	
	./script file1 file2
	a
	b
	c

	
	

### percentage\_output_loading.py
This snippet takes a text file, reads in each line, and whilst doing so gives a constantly updating percentage of it's progress.

### visio\_covert\_tms\_to\_vdx.py
This script will take an input tms file and convert it into a vdx file. Visio works better with vdx files rather than tms files.

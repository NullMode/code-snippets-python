#!/usr/bin/python
from __future__ import division
from time import sleep
import sys

# Set input file and sleep time
file_name = 'input.txt'
sleep_amount = 0.05


test_file = open(file_name, 'r').readlines()
line_count = len(test_file)

c = 1
for i in test_file:
	sys.stdout.write('\r')
	value = int(round((c / line_count) * 100))
	sys.stdout.write(str(value) + "%") 
	sys.stdout.flush()
	c = c + 1
	sleep(sleep_amount)
sys.stdout.write("\n")

#!/usr/bin/env python
from myutils import scanner
def firstword(line):
	print line.split( )[0]
input = open("list")
for line in input:
	line = line.rstrip('\n')
	print line
input.close()

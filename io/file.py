#!/usr/bin/env python
import sys

# read file
try:
	f = open("find.py", "r")
	try:
		for line in f:
			print line;
	finally:
		f.close()
except IOError as e:
	print "IO error ({0}): {1}".format(e.errno, e.strerror)

# write to file
try:
	with open("data", "r+") as f:
		f.write("I can write to python file\n");
		f.write("Yeah, it's great\n");
		f.seek(0)
		for line in f:
			# print without a newline
			sys.stdout.write(line)
except IOError as e:
	print "IO error {0}: {1}".format(e.errno, e.strerror)
except:
	print "Unexcepted error:", sys.exc_info()[0]

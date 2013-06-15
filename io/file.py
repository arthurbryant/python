#!/usr/bin/env python
import sys

try:
	f = open("find.py", "r")
	for line in f:
		print line;
	f.close();
except IOError as e:
	print "IO error ({0}): {1}".format(e.errno, e.strerror)

try:
	f = open("data", "r+")
	f.write("I can write to python file\n");
	f.write("Yeah, it's great\n");
	f.seek(0)
	for line in f:
		# print without a newline
		sys.stdout.write(line)
	f.close()
except IOError as e:
	print "IO error {0}: {1}".format(e.errno, e.strerror)
except:
	print "Unexcepted error:", sys.exc_info()[0]

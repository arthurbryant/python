#!/usr/bin/env python

try:
	f = open("find.py", "r")
	print "file opened"
	try:
		f.read(10)
	finally:
		f.close()
		print "file closed"
except IOError:
	pass

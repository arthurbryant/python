#!/usr/bin/env python

f = open("test")
line = f.readline().strip()
if "title" == line:
    line = f.readline().strip()
    if not line:
        print "null"
line = f.readline()
print line

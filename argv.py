#!/usr/bin/python 
import sys

if len(sys.argv) < 2:
    print "Usage: ./argv.py input"
    sys.exit(-1) 
else:
    for arg in sys.argv[1:]:
        print arg

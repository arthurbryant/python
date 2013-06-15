#!/usr/bin/env python
import sys

f = open("text")
content = f.read()
print content 
sys.stdin.flush()

f.seek(0)
if True:
    lines = f.readlines()
    for line in lines:
        print line
    f.close()
try:
    f = open("noexist", "w")
    f.write("start")
    f.write("end")
finally:
    f.close()

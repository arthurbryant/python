#!/usr/bin/env python
f = open("a.py")
line = f.readline()
print line
while True:
    l = f.readline()
    if not l:
        break
    print l
f.close()

#!/usr/bin/env python
import re

p = re.compile("(person\/|(institute|department)\.php\?id=)(\d+) ")
p2 = re.compile("search\.php\?query=(.*) HTTP")
with open("text") as f:
    for line in f.readlines():
        res = p.search(line)
        res2 = p2.search(line)
        if res:
            print res.group(3)
        else:
            print "not found"
        if res2:
            print res2.group(1)
        else:
            print "not found too"
        '''
str = "abc efd cd"
res = p.match(str)
if res:
    print res.group()
else:
    print "not found"

res2 = p.findall(str)
if res2:
    print res2
else:
    print "not found"
    '''

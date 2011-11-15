#!/usr/bin/env python
import sys

def p(*argv, **dict):
    for a in argv:
        print a
    print argv[0]
    print argv[1]
    for d in dict:
        print d
#p(*sys.argv[1:])
m = ('a', 'aa', 'aaa')
n = {'name':'arthur', 'age':24}
p(*m, **n)
p(*sys.argv[1:])

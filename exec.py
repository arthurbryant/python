#!/usr/bin/env python
from math import sqrt

scope = {}
exec 'sqrt = 1' in scope
print sqrt(4)
print scope['sqrt']
print len(scope)
print scope.keys()
exec 'print "hello, world"'

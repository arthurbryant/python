#!/usr/bin/env python
try:
    a = 1/0
except Exception, e:
    print "bad:", e

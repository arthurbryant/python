#!/usr/bin/env python
try:
    print "Enter date" 
    print "Month?"
    A = input()
    A = (A+9)%12+1 
    print "Day?" 
    B = input()
    print "Year?" 
    C = input()
    print "Century?" 
    D = input()
    print A, B, C, D
    W = (13*A-1)/5
    X = C/4
    Y = D/4
    Z = W+X+Y+B+C-2*D
    R = (Z%7+7)%7
    print "The", (R+1), "day of the week" 
except Exception, e:
    print e

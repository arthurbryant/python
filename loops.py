#!/usr/bin/env python
'''
while True:
    print "Please input base"
    base = input()
    print "Please input exp"
    exp = input()
    print "Result: ", base**exp
'''
try:    
    while True:
        print "Enter an even number"
        even = input()
        if(even % 2 == 0):
            print "OK"
            break
        else:
             continue
except Exception, e:
    print e

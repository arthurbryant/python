#!/usr/bin/python2

n = 10
i = 10
while i > 0:
    print i
    if i % 2 == 0:
        n = i / 2
    else:
        i = i + n 

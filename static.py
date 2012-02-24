#!/usr/bin/env python
global count
def f(m, n, size):
    print m[count]%n, n
    count = (count+1) % size 
count = 0
m=('http://10.10.104.13:80%s', 'http://10.10.104.80:80%s')
n=('ab', 'cd', 'def')
size = len(m)
for c in n:
    f(m, c, size)

#!/usr/bin/env python
count = 0
def f(m, n, size):
    global count
    print m[count]%n, n
    count = (count+1) % size 
m=('http://10.10.104.13:80%s', 'http://10.10.104.80:80%s')
n=('/ab', '/cd', '/def', '/aaa')
size = len(m)
for c in n:
    f(m, c, size)

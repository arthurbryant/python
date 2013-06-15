#!/usr/bin/env python
str = "I am so sorry!"
result = [] 
base = 0
lstr = list(str)
print lstr
for s in lstr:
    if s != '':
        if s.isalpha():
            if s.islower():
                base = ord('a')
            else:
                base = ord('A')
            s = chr((ord(s) - base + 1)%26 + base)
            print s
    result.append(s)
print lstr
print result 
print "".join(result)

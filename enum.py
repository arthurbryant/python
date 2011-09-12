#!/usr/bin/env python
strings = ['good luck', 'goodbye', 'good night', 'lovely']
key  = "good"
'''
for string in strings:
    if key in string:
        index = strings.index(string)
        strings[index] = 'censored'
print strings
index = 0
for string in strings:
    if key in string:
        strings[index] = 'censored'
    index += 1
#print index
'''
print strings
for index,string in enumerate(strings):
    if key in string:
        strings[index] = 'censored'
print strings

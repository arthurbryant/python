#!/usr/bin/env python
result = open('a.py')
r = result.readline()
print(r)
r = result.readline()
print(r)

r = result.readline()
print(r)
r = result.readline()
if r == "":
    print("end")
r = result.readline()
if r == "":
    print("end")

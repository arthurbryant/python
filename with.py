#!/usr/bin/env python

with open("with.py") as f:
    for l in f:
        print l,

def collection():
    print("collection function")

for thing in collection():
    print("execute only once")

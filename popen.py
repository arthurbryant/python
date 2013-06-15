#!/usr/bin/python
import os

str = os.popen('ls -l ').readlines()
for line in str:
    print line

#!/usr/bin/env python
import fileinput
for line in fileinput.input("input.py"):
    print line,

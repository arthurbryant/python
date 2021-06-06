#!/usr/bin/env python

# zhangfeng
# arguments.py
# 2012-02-20

import sys

def a(x, y=3):
    return x+y
print a(1)
print a(2, 2)
print a(y=10, x=12)

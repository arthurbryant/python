#!/usr/bin/env python
def g():
    def f():
        x = 20
        print x
        x += 1
        return x
    f()
    f()
g()

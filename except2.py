#!/usr/bin/env python
try:
    float(['abc', 1])
except TypeError, diag:
    pass
print type(diag)
print diag
print diag.__class__
print diag.__class__.__doc__
print diag.__doc__
print diag.__class__.__name__

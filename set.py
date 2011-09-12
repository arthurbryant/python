#!/usr/bin/env python
myset = []
for i in range(10):
    print i
    myset.append(set(range(i, i+5)))
result = reduce(set.union, myset)
print result

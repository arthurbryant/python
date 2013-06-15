#!/usr/bin/env python
from heapq import *
from random import shuffle

data = range(10)
shuffle(data)
print data
heap = []
for i in data:
    heappush(heap, i)
print heap
heappop(heap)
print heap
heappop(heap)
print heap

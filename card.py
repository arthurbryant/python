#!/usr/bin/env python
from random import *
from pprint import pprint

values = range(1, 11) + 'J, Q, K'.split()
print values
suits = ['diamonds', 'spades', 'clubs', 'hearts']
deck = ['%s of %s' % (v, s) for v in values for s in suits]
deck += ['S', 's']
shuffle(deck)
pprint(deck)
print len(deck)
deck.pop()
deck.pop()
a = b = c = d = [] 
while deck:
    a.append(deck.pop())
pprint(a)
'''
print b
print c
print d
'''

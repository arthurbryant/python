#!/usr/bin/env python
boys = ['arthur', 'bryant', 'tom']
girls = ['alice', 'tim', 'bob']
a = [b + '+' + g for b in boys for g in girls if b[0] == g[0]]
print a

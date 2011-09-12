#!/usr/bin/env python
boys = ['arthur', 'bryant', 'tom']
girls = ['alice', 'tim', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print [b + '+' + g for b in boys for g in letterGirls[b[0]]] 

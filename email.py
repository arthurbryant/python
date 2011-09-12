#!/usr/bin/env python
import re, fileinput

'''
p = re.compile(r'From: (.*)<.*?>')
for line in fileinput.input():
    m = re.search(p, line)
    if m:
        print m.group(1)
'''
p = re.compile(r'[\w\-\.]+@[\w\-\.]+')
addresses = set()
for line in fileinput.input():
    for address in p.findall(line):
        addresses.add(address)
for address in sorted(addresses):
    print address

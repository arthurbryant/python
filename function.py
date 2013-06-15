#!/usr/bin/env python
flag = 0
process = flag and (lambda s: " ".join(s.split())) or (lambda s: s)
print process("that is \n terrific")

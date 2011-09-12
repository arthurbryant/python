#!/usr/bin/env python
import re

p1 = re.compile(r'\*([^\*]+)\*')
p2 = re.compile(r'\*(.*?)\*')
result = re.sub(p2, r'<em>\1</em>', r"hello, **something**")
print result

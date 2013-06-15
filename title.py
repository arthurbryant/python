#!/usr/bin/env python
import re
import sys

p = re.compile("<title>", re.I)
q = re.compile("</title>", re.I)
f = open('a')
content = f.read()
result = p.search(content)
print result
start = result.end() 
result = q.search(content, start)
end = result.start()
substr = content[start:end]
print substr

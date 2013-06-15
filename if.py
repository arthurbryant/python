#!/usr/bin/env python
import re
p = re.compile("\.edu\.cn")
result = p.search("xjtu.edu.cn")
if result is None:
	print "match"
else:
	print result.group()

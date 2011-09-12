#!/usr/bin/env python
import sys
import string
str = ".? what are"
str = str.strip(string.punctuation)
str = str.strip()
str = str.strip(string.punctuation)
str = str.strip()
print str

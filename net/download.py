#!/usr/bin/env python

import urllib

try:
	url = "http://mail.sina.com.cn/"
	sina = urllib.urlopen(url)
	try:
		sina_data = sina.read()
	finally:
		sina.close()
	f = open('sina_data', 'w')
	try:
		f.write(sina_data)
		print "write to file"
	finally:
		f.close()
except IOError:
	print "IOError"


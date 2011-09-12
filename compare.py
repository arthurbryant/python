#!/usr/bin/env python
file1 = open("1.txt");
str1 = file1.readline();
file2 = open("2.txt");
str2 = file2.readline();
if(str1 == str2):
	print "ok"
flag = True

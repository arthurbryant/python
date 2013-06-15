#!/usr/bin/env python
base = 2000
profit = 0.1
total = 0
year = int(raw_input("Please input the year\n"))
print year
count = 1
while count <= year:
	total += base + total * profit
	count = count + 1
	print count
print total


#!/usr/bin/env python
import time

def cost_time(func):
	def	result (*args, **dic):
		beign = time ()
		func (*args, **dic) 
		print "cost time : ", time () - beign 
		return result 

@cost_time 
def show(n):
	for x in range(n):
		print x
show(10)

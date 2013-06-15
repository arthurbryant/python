#!/usr/bin/env python
import math
import random

def ran_div_is_3():
    return random.randint(0, 100) % 3 == 0
for i in range(20):
    print ran_div_is_3()
def roll_dice(max, num):
    for i in range(num):
        print random.randint(1, max)
    print "That's all"
roll_dice(6, 4)
roll_dice(14, 8)
               

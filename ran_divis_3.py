#!/usr/bin/env python
import math
import random

def ran_div_is_3:
    return random.randint(0, 100) % 3 == 0
for i in range(20):
    print ran_div_is_3(i)

#!/usr/bin/env python
import math

def multadd(a, b, c):
        return (((a)*(b))-c) 
def yikes(x):
    return multadd(x, (math.e)**(-x), -math.sqrt(1-(math.e)**(-x)))
print multadd(math.cos(math.pi/4), 1/2.0, -math.sin(math.pi/4))
print multadd(2, math.log(12.0, 7),-math.ceil(276/19.0))                                                        
print yikes(5)
                                                                                                                

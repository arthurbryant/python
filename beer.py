#!/usr/bin/env python
REFRAIN = '''
%d bottles of beer
    take one down
    %d bottles of beer on the wall
    '''
beer = 20

while beer > 1:
    print REFRAIN % (beer, beer - 1)
    beer -= 1

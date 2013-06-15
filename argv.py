#!/usr/bin/python 
import sys

class person:
    name = ''
    age = 0
    purpose = ''
    def __init__(self, *argv):
        i = 0
        for arg in argv:
            print arg, "\n"
            if(i == 0):
                self.name = arg 
            elif(i == 1):
                self.age = arg 
            else:
                self.purpose += arg 
            i = i+1
            print i
    def display(self):
        print  'name=', self.name, 'age=', self.age, 'purpose=', self.purpose

if len(sys.argv) < 3:
    print "Usage: ./argv.py input"
    sys.exit(-1) 
else:
    print sys.argv[1:]
    print sys.argv[1]
    p = person(sys.argv[1:])
    p.display()

#!/usr/bin/env python
import glob
python_files = glob.glob('*.py')
for fn in python_files:
    print '----', fn
    for line in open(fn):
        print '    ', line.rstrip()
    print

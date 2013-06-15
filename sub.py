#!/usr/bin/env python
import subprocess

str = subprocess.check_output(['ls'])
print str

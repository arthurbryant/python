#!/usr/bin/env python
import re
for test_string in ['555-1212', 'abc-defe']:
    if re.match('^\d{3}-\d{4}$', test_string):
        print test_string, 'is valid'
    else:
        print test_string, 'is not a phone number'


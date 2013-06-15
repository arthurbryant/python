#!/usr/bin/env python
try:
	x = int(raw_input('please input number:'))
except ValueError:
	print 'not number'
except:
	pass
else:
		print 'result = ', x
finally:
	print 'finish'

#!/usr/bin/env python
import datetime
import time
import calendar

str = "16/Nov/2010:16:12:29"
#res = datetime.datetime.fromtimestamp(str)
dt = time.strptime(str, "%d/%b/%Y:%H:%M:%S")
utc = datetime.datetime(dt.tm_year, dt.tm_mon, dt.tm_mday, dt.tm_hour, dt.tm_min, dt.tm_sec)
print utc.time() 
print time.time()
#print calendar.timegm(utc)
print time.mktime(dt)

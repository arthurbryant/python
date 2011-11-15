#!/usr/bin/env python
import time
try:
    try:
        while True:
           time.sleep(2) 
           print "sleep"
           a = 1/0
    #except (KeyboardInterrupt, Exception), e:
    #    print "error:", e 
    except KeyboardInterrupt, e:
        print "keyboard", str(e) 
    except Exception, e:
        print e
finally:
    print "final"

#!/usr/bin/env python
import  urllib

pat = "http://10.10.97.116:80/search.php?query=%s"
req = "a"
result = pat%urllib.quote_plus(req), req
print result

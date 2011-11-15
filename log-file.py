#!/usr/bin/env python
import logging
level = getattr(logging, loglevel.upper(), None)
if not isinstance(level, int):
    raise ValueError("Invalid log level %s" % loglevel)
logging.basicConfig(filename="example.log", level=level)

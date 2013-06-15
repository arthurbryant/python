#!/usr/bin/env python
import MYSQLdb

con = MYSQLdb.connect('10.10.104.13', 3306, 'root', '@RSadmin123', 'htc-testbed')
con.close()

#!/usr/bin/python

import sys
from datetime import datetime

for line in sys.stdin:
    l=line.split("\t")
    try:
        day=datetime.strptime(l[0], "%Y-%m-%d").weekday()
        sales=l[4]
        print "{0}\t{1}".format(day, sales)
    except:
        pass
      

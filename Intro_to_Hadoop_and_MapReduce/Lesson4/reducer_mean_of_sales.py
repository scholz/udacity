#!/usr/bin/python

import sys
import numpy as np

sum=0.
count=0
for line in sys.stdin:
    day,sale=line.split("\t")
    if day.isdigit() and int(day)==6:
        try:
            sum+=float(sale)
            count+=1
        except:
            pass

print "Number of Sales: %i, Sum of Sales: %i, Average Sale: %f"%(count, sum, sum/count)

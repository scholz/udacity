#!/usr/bin/python

import sys
import numpy as np

sum=[0.]*7
count=[0]*7
for line in sys.stdin:
    day,sale=line.split("\t")
    if day.isdigit():
        day=int(day)
        try:
            sum[day]+=float(sale)
            count[day]+=1
        except:
            pass

for i in range(len(sum)):
    if count[i]>0:
        print "{0}\t{1}".format(i, sum[i]/count[i])

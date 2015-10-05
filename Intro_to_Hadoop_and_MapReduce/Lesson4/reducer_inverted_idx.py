#!/usr/bin/python

import sys
count=0
nodes=[]
for line in sys.stdin:

    words=line.split("\t")
    node=words[0]
    for w in words[1:]:
        if w=='fantastic':
            count+=1
        if w=='fantastically':
            nodes.append(int(node))
     
print "Occurences of fantastic:", count
print "Nodes containing fantastically:", sorted(nodes)

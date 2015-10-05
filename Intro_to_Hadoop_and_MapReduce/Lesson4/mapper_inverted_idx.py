#!/usr/bin/python

"""
Mapper for Udacity MapReduce Introduction on Udacity, Lesson 4
Task: Counting the occurences of fantastic and identifying the node_ids
  where the word fantastically occurs
"""
import re
import sys

node="-1"
current_line=[]

# skip header
next(sys.stdin)

for line in sys.stdin:

    l=line.lower()

    # split line
    words=filter(None, re.split('\W+', l))
 
    if len(words)>1 and words[0].isdigit():
        if node!="-1":
            print "{0}\t{1}".format(node, "\t".join(current_line))
        node=words[0]
        current_line=words[1:]
    else:
        current_line+=words
    


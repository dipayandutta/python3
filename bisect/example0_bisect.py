# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 12:58:26 2018

@author: node
"""
'''
The bisect module implements an algorithm for inserting elements into a list while 
maintaining the list in sorted order
'''
import bisect

values = [10,12,23,44,56,9,4,-3,11]

l = []
for i in values:
  position = bisect.bisect(l,i)
  bisect.insort(l,i)
  
  print('{:3} {:3}'.format(i,position),l)
  
print ('Unsorted List {}'.format(values))
print ('Sorted List {}'.format(l))
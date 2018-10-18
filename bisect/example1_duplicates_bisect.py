# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:03:15 2018

@author: node
"""

import bisect 
#Handleing duplicate entry
values = [10,20,-9,8,6,12,10,30,-7,0,33,100,33]

l = []
for i in values:
  position = bisect.bisect_left(l,i)
  bisect.insort_left(l,i)
  
  print ('{:3} {:3}'.format(i,position),l)
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 08:17:17 2018

@author: node
"""

# zip to create a tuple from two list
first_list = [x for x in range(1,10)]
second_list = [y for y in range(11,20)]

for i in zip(first_list,second_list):
  print(i,end=' ')
  
  
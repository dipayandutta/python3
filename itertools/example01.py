# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 08:12:27 2018

@author: node
"""
from itertools import chain 
sample_list = [x for x in range(1,10)]
second_sample_list = [y for y in range(11,20)]

for i in chain(sample_list,second_sample_list):
  print(i,end='')
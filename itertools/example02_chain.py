# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 08:15:35 2018

@author: node
"""

from itertools import *

def make_itertables_to_chain():
  yield[1,2,3]
  yield['a','b','c']
  
for i in chain.from_iterable(make_itertables_to_chain()):
  print(i,end='')
  
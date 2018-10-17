# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:34:07 2018

@author: node
"""

import collections
import random

random.seed(1)

d1 = collections.deque(maxlen=3)
d2 = collections.deque(maxlen=3)


for i in range(5):
  n = random.randint(0,100)
  print(n)
  d1.append(n)
  d2.appendleft(n)
  
  print(d1)
  print(d2)

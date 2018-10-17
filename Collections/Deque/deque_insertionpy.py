# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 09:47:19 2018

@author: node
"""

import collections

d1 = collections.deque()
d1.extend('abcd')
print(d1)

d1.append('ef')
print(d1)

d2 = collections.deque()
d2.extendleft(range(10))
print(d2)
d2.appendleft(11)
print(d2)
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:20:40 2018

@author: node
"""

import collections

d = collections.deque()
d.extend(range(10))
print(d)
d.rotate(2)
print('Right Rotation ',d)

# Left Rotation
d.rotate(-2)
print('Left Rotation',d)
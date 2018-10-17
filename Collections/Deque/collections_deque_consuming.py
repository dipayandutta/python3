# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:18:04 2018

@author: node
"""

import collections

print('From the Right')
d = collections.deque('abcdef')

while True:
  try:
    print(d.pop(),end='')
  except IndexError:
    break
  
  
print()

print ('From the Left')
d = collections.deque(range(10))

while True:
  try:
    print(d.popleft(),end='')
  except IndexError:
    break
  
print()
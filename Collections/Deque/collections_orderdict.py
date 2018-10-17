# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 11:01:15 2018

@author: node
"""

import collections

print('Regular Dict...')
d = {}
d['a'] = 'A'
d['c'] = 'C'
d['b'] = 'B'

print (d)

for k,v in d.items():
  print (k,v)
  
# In ordered dict , by constract the order in which the items are inserted is remembered and used when creating an iterator.
  
d = collections.OrderedDict()
d['b'] = 'B'
d['a'] = 'A'

for k,v in d.items():
  print(k,v)
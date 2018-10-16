# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 00:52:41 2018

@author: node
"""

import collections

def default_dict():
  return 'default value'

d = collections.defaultdict(default_dict,foo='bar')
print (d)
print(d['foo'])
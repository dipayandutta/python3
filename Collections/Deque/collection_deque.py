# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 09:20:21 2018

@author: node
"""

import collections

d = collections.deque('abcdef')
print (d)
print ('Length of the Deque is {}'.format(len(d)))
print ('Left End {}'.format(d[0]))
print ('Right End {}'.format(d[-1]))
print(d.remove('c'))
print(d)
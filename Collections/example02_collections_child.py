# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 00:25:14 2018

@author: node
"""

import collections 

a = {'a':'A','b':'B'}
b = {'c':'C','d':'D'}
c = {'c':'E'}

m1 = collections.ChainMap(a,b)
m2 = m1.new_child(c)


print (m1['c'])
print (m2['c'])
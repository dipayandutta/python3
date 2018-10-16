# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 00:32:10 2018

@author: node
"""

# A counter is a container that keeps track of how many times equivalent values are added

import collections

print (collections.Counter(['a','v','a']))

c = collections.Counter('Hello World')
print (c)
print (c['l'])
print (list(c.elements()))
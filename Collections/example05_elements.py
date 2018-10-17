# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 11:08:55 2018

@author: node
"""

import collections

c = collections.Counter(a=2,b=3,c=4)
print(c)
print(sorted(c.elements()))

#finding the most common 
most_common = collections.Counter('aabsdbdwdasdda').most_common(3)
print("Most Common Three words are {}".format(most_common))

c = collections.Counter(a=3,b=2)
d = collections.Counter(a=1,b=4)

print('Adding Two Counters {}'.format(c+d))
print('Subtracting Two Counters {}'.format(c-d))
print('Inersection of two Counters {}'.format(c&d))
print ('Union of two counters {}'.format(c | d))
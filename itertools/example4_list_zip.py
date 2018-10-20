# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 08:19:11 2018

@author: node
"""

from itertools import *

r1 = range(3)
r2 = range(4)

print ('After Zip')
print (list(zip(r1,r2)))

r1 = range(4)
r2 = range(3)

print ('After zip longest')
print(list(zip_longest(r1,r2)))

r1 = [x for x in range(1,5)]
r2 = [x for x in range(3,10)]

print(r1)
print(r2)

# list concatination of two lists
r3 = r1+r2
print(r3)

for item in chain(r1,r2):
  print (item)
  
# use set to get the unique values from the two lists after merged
  
mergedlist = list(set(r1+r2))

print(mergedlist)


a = [[1,2,3],[4,5,6],[7,8,9]]
merged_list = [x for xs in a for x in xs]
print (merged_list)
print("Using itertools")
print(list(chain(*a)))
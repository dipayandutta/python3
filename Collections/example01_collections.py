# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 22:45:47 2018

@author: node
"""

'''
ChainMap class manages a sequnce of dictonaries and searches through them in the order they appear to find the values associated with keys
'''
import collections

a = {'a':'A','b':'B'}
b = {'c':'C','d':'D'}

m = collections.ChainMap(a,b)
for key in a.keys():
  print (key)
  
print(m)

print ('Keys == {}'.format(list(m.keys())))
print ('Values == {}'.format(list(m.values())))
  
for key,value in m.items():
  print('{}==>{}'.format(key,value))
  
print ('c= {}'.format(m['c']))

#updateing an item in the dictonary
m['c'] = 'E'
print ('Current c = {}'.format(m['c']))
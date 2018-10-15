# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 18:45:01 2018

@author: node
"""

import re

regexs = [re.compile(p) for p in ['this','that']]

text = 'Does this text match the pattern ?'

print ('Text: {!r}\n'.format(text))

for regex in regexs:
  print('Seeking "{}" ->'.format(regex.pattern),end='')
  
  if regex.search(text):
    print ('Match!')
  else:
    print('No Match!')
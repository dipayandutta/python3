# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 19:11:45 2018

@author: node
"""

import re

text = 'This is some text  -- with punctuation'
pattern = re.compile(r'\b\w*is\w*b')

print('Text:',text)
print()

pos =0
while True:
  match = pattern.search(text,pos)
  if not match:
    break
  
  start = match.start()
  end   = match.end()
  
  print (text[start:end])
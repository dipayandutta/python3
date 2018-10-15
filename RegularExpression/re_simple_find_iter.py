# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 18:51:11 2018

@author: node
"""

import re

text = 'aaabbbbabababbbaa'

pattern = 'ab'

for match in re.finditer(pattern,text):
  start = match.start()
  end   = match.end()
  print('Found {!r} at {:d}:{:d}'.format(text[start:end],start,end))
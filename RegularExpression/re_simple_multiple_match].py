# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 18:50:04 2018

@author: node
"""

import re

text = 'aabbbaaaabb'

pattern = 'ab'

for match in re.findall(pattern,text):
  print (match)
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 12:59:00 2018

@author: node
"""

import hashlib
import time

# Calculate md5 checksum
data = open(__file__,'rb').read()
print(data)

for i in range(5):
  h = hashlib.sha1()
  print(time.ctime(),':{:0.3f} {:0.3f}'.format(time.time(),time.clock()))
  for i in range(30000):
    h.update(data)
  checksum = h.digest()
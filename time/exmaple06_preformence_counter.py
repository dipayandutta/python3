# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 13:11:05 2018

@author: node
"""

import time 
import hashlib

data = open(__file__,'rb').read()
start_loop = time.perf_counter()

for i in range(5):
  iter_start = time.perf_counter()
  h = hashlib.sha1()
  for i in range(300000):
    h.update(data)
  ckhsum = h.digest()
  now = time.perf_counter()
  
  loop_elapsed = now-start_loop
  iter_elapsed = now-iter_start
  
  print(time.ctime(),':{:0.3f} {:0.3f}'.format(loop_elapsed,iter_elapsed))

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:11:58 2018

@author: node
"""

import queue

q = queue.LifoQueue()

for i in range(10):
  q.put(i)
  
# Displaying items in the queue
while not q.empty():
  print(q.get(),end='')
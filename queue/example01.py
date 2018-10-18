# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:06:45 2018

@author: node
"""

import queue

q = queue.Queue() #Creating the Queue object

#inserting elements in the Queue
for i in range(5):
  q.put(i)
  
# Displaying elements from the queue
while not q.empty():
  print(q.get(),end='')
  
  
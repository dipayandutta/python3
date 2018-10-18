# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:13:41 2018

@author: node
"""

import functools
import queue
import threading

@functools.total_ordering

class Job:
  
  def __init__(self,priority,description):
    self.priority = priority
    self.description = description
    print('New Job:',description)
    
    return 
  
  def __eq__(self,other):
    try:
      return self.priority == other.priority
    except AttributeError:
      return NotImplemented
    
  def __lt__(self,other):
    try:
      return self.priority < other.priority
    except AttributeError:
      return NotImplemented
    
q = queue.PriorityQueue()
q.put(Job(3,'Mid Level Job'))
q.put(Job(10,'Low Level Job'))
q.put(Job(1,'Important Job'))

def process_job(q):
  while True:
    next_job = q.get()
    print ('Processing jobs: ',next_job.description)
    q.task_done()

workers = [threading.Thread(target=process_job,args=(q,)),
           threading.Thread(target=process_job,args=(q,)),
           ]

for work in workers:
  work.setDaemon(True)
  work.start()
  
q.join()
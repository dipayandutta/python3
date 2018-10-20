# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 13:07:59 2018

@author: node
"""

import time 

template = '{} -{:0.2f} - {0.2f}'

print('{} -{:0.2f} - {0.2f}'.format(time.ctime(),time.time(),time.clock()))
for i in range(3,0,-1):
  print ('Sleeping',i)
  time.sleep(i)
  print(template.format(time.ctime(),time,time(),time.clock()))
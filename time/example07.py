# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 13:40:48 2018

@author: node
"""

import time

def show_struct(s):
  print(' tm_year :',s.tm_year)
  print(' tm_month:',s.tm_mon)
  print(' tm_mday:',s.tm_mday)
  
  
print('gmtime')
show_struct(time.gmtime())
show_struct(time.localtime())
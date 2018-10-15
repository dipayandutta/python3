# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 21:36:30 2018

@author: node
"""

import enum

class BugStatus(enum.Enum):
  
  new = 10
  incomplete = 12
  wont_fix = 1
  fix_released = 1.2
  

actual_state = BugStatus.wont_fix
desired_state = BugStatus.fix_released

print('Equality ',actual_state == desired_state)
  
for members in BugStatus:
  print (members.name)
  print (members.value)
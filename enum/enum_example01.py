# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:23:58 2018

@author: node
"""

import enum

class BugStatus(enum.Enum):
  
  new = 10
  incomplete = 121
  
print ('Member Name: {}'.format(BugStatus.incomplete.name))
print ('Memeber Value: {}'.format(BugStatus.incomplete.value))


for members in BugStatus:
  print('{:12} = {}'.format(members.name , members.value))
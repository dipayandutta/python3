# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 21:48:43 2018

@author: node
"""

import enum

class BugStatus(enum.Enum):
  
  new = (7,['incomplete','invalid','wont fix'])
  incompelete = (6,['new','wont_fix'])
  invalid = (5,['new'])
  wont_fix = (4,['new'])
  fix_released = (1,['new'])
  
  def __init__(self,num,transitions):
    self.num = num
    self.transitions = transitions
    
  def can_transition(self,new_state):
    return new_state.name in self.transitions
  
  
print ('Name: ',BugStatus.incompelete.name)
print ('Values: ',BugStatus.incompelete.value)
print('Using Attribute',BugStatus.incompelete.can_transition(BugStatus.new))
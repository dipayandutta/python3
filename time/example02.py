# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 12:52:03 2018

@author: node
"""

import time 

print ('Current time is {0}'.format(time.ctime()))
later = time.time() +15 # 15 secs later time shall be
print ('Future time 15 secs later {0}'.format(time.ctime(later)))
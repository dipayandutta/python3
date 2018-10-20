# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 13:43:19 2018

@author: node
"""

import datetime

today = datetime.date.today()
print (today) # Current date
print ('ctim {}'.format(today.ctime()))

tt = today.timetuple()
print('Year {}'.format(tt.tm_year))
print ('Month {}'.format(tt.tm_mon))
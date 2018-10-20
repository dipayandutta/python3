# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 12:56:53 2018

@author: node
"""

import time

start = time.monotonic()
time.sleep(1)
end = time.monotonic()

elapsed = end - start
print('Start time {}'.format(start))
print ('End Time {}'.format(end))
print ('Elapsed time {}'.format(str(elapsed)))
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:38:41 2018

@author: node
"""

import re

pattern = 'this'
text = 'this is the planet earth'

match = re.search(pattern,text)

print(match)

start = match.start()
end   = match.end()

print (start)
print (end)

print ('Found "{}\n in "{}"\n form {} to {} ("{}")' .format(match.re.pattern,match.string,start,end,text[start:end]))
       
       
      
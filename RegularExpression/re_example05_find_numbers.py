# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 18:40:38 2018

@author: node
"""

import re 

string = 'My 2 fav numbers are 5 and 7'

numbers = re.findall(r'[0-9]+',string)

print(numbers)
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 12:45:50 2018

@author: node
"""

import re

text = "Hello World Planet100"
search = re.findall(r'\D',text)

print (search)

# split the string
string_list = []
string_list.append(((re.split(r'\s','The string to split'))))

print (string_list)

for character in string_list :
  print (character)


for character in string_list:
  print ("Length of the string is {}".format(len(character)))
  for x in range(len(character)):
    print (character[x])
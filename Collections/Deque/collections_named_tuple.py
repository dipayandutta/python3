# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:38:13 2018

@author: node
"""

import collections

Person = collections.namedtuple('Person','name age')

bob = Person(name='Bob',age=20)
print('Name {}'.format(bob.name))
print('Age: {}'.format(bob.age))

jane = Person(name='Jane',age=20)

for person in [bob,jane]:
  print(*person)
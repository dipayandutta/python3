# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:25:47 2018

@author: node
"""

import textwrap
from textwrap_example import sample_text

dedent_text = textwrap.dedent(sample_text).strip()
for width in [45,60]:
  print('{} Columns:\n'.format(width))
print(textwrap.fill(dedent_text,width=width))
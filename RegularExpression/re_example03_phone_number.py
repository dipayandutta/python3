# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:03:47 2018

@author: node
"""

import re

def detect_numbers(text):
    phone_regex = re.compile(r"(\+420)?\s*?(\d{3})\s*?(\d{3})\s*?(\d{3})")
    groups = phone_regex.findall(text)
    for g in groups:
        print("".join(g))

detect_numbers("so I need to match +420 123 123 123, also 123 123 123, also +420123123123 and also 123123123. Can y")
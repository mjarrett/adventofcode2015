#!/usr/bin/python

"""
created by Mike Jarrett
"""

import re

f = open('input.txt','r')
text = f.read()

ups = re.findall(r'\(', text)
downs = re.findall(r'\)', text)

print len(ups)
print len(downs)

print len(ups) - len(downs)

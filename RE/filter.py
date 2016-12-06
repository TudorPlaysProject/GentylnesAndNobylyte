#!/usr/bin/python
import fileinput
import string
for line in fileinput.input():
    line = line.replace('\n', '') # 10
    line = line.replace('.', '')  # 46 
    line = line.replace('V', 'U') # 85-86
    line = line.replace('v', 'u') # 117-118
    print line.lower()

#!/usr/bin/python
#title			:day6.py
#description		:Day 6 advent of code
#author			:Mike Jarrett
#date			:20151225
#version		:1
#usage			:python day6.py
#notes			:
#python_version	:2.6.6
#==============================================================================

import re


f = open('input.txt')
#f = open('test.txt')

#build grid

grid = {} # 1000x1000 grid
grid2 = {}

for i in range(0,1000):
    for j in range(0,1000):
        grid[(i,j)] = False
        grid2[(i,j)] = 0

for line in f:
    match = re.search('(\w+) (\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})',line)
    if match:
        
        x1 = int(match.group(2))
        y1 = int(match.group(3))
        x2 = int(match.group(4))
        y2 = int(match.group(5))
        

        for x in range(x1,x2+1):
            for y in range(y1,y2+1):

                if match.group(1) == 'on':
                    grid[(x,y)] = True
                    grid2[(x,y)] += 1
                elif match.group(1) == 'off':
                    grid[(x,y)] = False
                    grid2[(x,y)] -= 1
                    if grid2[(x,y)] < 0: grid2[(x,y)] = 0
                elif match.group(1) == 'toggle':
                    grid[(x,y)] = not grid[(x,y)]
                    grid2[(x,y)] += 2
print(sum(grid.values()))        
print(sum(grid2.values()))
    




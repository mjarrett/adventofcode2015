#!/usr/bin/python
#title			:day5.py
#description		:day 5 advent of code
#author			:Mike Jarrett
#date			:20151223
#version		:1
#usage			:python day5.py
#notes			:
#python_version	:2.6.6
#==============================================================================

#import re

vowels = [ 'a', 'e', 'i', 'o', 'u' ]
badstrings = [ 'ab', 'cd', 'pq', 'xy' ]

def threevowels(line):
    threevow = False
        
    count = 0
#    print line

    for vowel in vowels:
            
        if vowel in line:
            #print vowel
            count += 1
            #print count
            #print line
            if count == 3:
                threevow = True
                #print line
                break
    return threevow

def hasdoubles(line):
    hasdoubs = False
    for i, c in enumerate(line):  #i gives index, c gives character

        if i != 0:
            if line[i] == line[i-1]:

                hasdoubs = True 
        #    break
    return hasdoubs
        
def nobads(line):
    nobad = True

    for i, c in enumerate(line):
        if i != 0:
            pair = line[i-1] + line[i]
            if pair in badstrings:
                print pair
                nobad = False
    return nobad

def goodstrings():

    f = open('input.txt')

#    f = [ 'ugknbfddgicrmopn', 'jchzalrnumimnmhp' , 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb' ]

    goodlines = 0
    for line in f:
        #print line

        if threevowels(line) and hasdoubles(line) and nobads(line):
        #if nobads(line):
            goodlines += 1
            
            print line
            #print goodlines
        #else: print line
    print goodlines




goodstrings()

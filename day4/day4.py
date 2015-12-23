#!/usr/bin/python
#title			:day4.py
#description		:Advent of code day 4
#author			:Mike Jarrett
#date			:20151222
#version		:1
#usage			:python day4.py
#notes			:
#python_version	:2.6.6
#==============================================================================
import hashlib
import itertools

def find_hash():


    secret_key = 'bgvyzdsv' #define my key
    
    for i in itertools.count(0):
        m = hashlib.md5() # create hash object
        test_hash = secret_key + str(i) # add test nuber to key
        m.update(test_hash) # hash the test string

        mh = m.hexdigest()
        if mh[0:5] == '00000':
            print mh
            print test_hash # print the test hash
            
        if mh[0:6] == '000000':
            print mh
            print test_hash
            break



    return mh


find_hash()

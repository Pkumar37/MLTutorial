#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 22:58:07 2017

@author: pkum37
"""

import numpy as np

filename = '/Users/pkum37/Desktop/phantomjs-2.1.1-macosx/third-party.txt'

file = open(filename , "r")

text = file.read()
file.close()

#print(text)

data= np.loadtxt(filename , delimiter=',' , dtype =str)
print (data)
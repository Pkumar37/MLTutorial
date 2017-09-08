#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 23:25:31 2017

@author: pkum37
"""
import numpy as np
h = 123
w= 62
a= 'aasff'
b='dfff'
k = [1.7,3.3,2.5,33,3.5]
bmi = h*w/2
z = k[3]

v = [1,2,3,4,5]
m=[2,4,5,6,7]
np_v= np.array(v)
np_m= np.array(m)
s= np_v+ np_m

y = ([1,3,6,9,11,13],[2,4,6,7,8,10])

o = np.array(y)
t = o[:,1:]
#print(t)

height = np.round(np.random.normal(1,1,100),2)
weight = np.round(np.random.normal(2,2,100),2)
np_city = np.column_stack((height,weight))
print(np_city[92:37])

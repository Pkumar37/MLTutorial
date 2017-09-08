#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 14:06:37 2017

@author: pkum37
"""


import matplotlib.pyplot as plt
from urllib.request import urlretrieve
import pandas as pd

a =[10,50,80,600]
b =[2.00,8.00,3.00,7.00]
plt.plot(a,b)
plt.show()

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
urlretrieve(url,'winequality-red.csv')
file = 'winequality-red.csv'
data = pd.read_csv(file)

data.head()

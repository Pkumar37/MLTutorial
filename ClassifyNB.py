#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 21:45:53 2017

@author: pkum37
"""
    
def classify(features_train, labels_train):   
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    return clf.fit(features_train,labels_train)
pred = clf.predict(feature_test)

from sklearn.metrics import accuracy_score
print (accuracy_score(pred, labels_test))
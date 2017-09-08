#!/usr/bin/python


from time import time
from email_preprocess import preprocess

features_train, features_test, labels_train, labels_test = preprocess()

from sklearn import svm
from sklearn.metrics import accuracy_score

linear_kernel_svm = svm.SVC(kernel='rbf', C=10000.)

features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

t0 = time()
linear_kernel_svm.fit(features_train, labels_train)
print ("training time", time() - t0)

t1 = time()
pred = linear_kernel_svm.predict(features_test)
print ("prediction time ", time() - t1)

acc = accuracy_score(labels_test, pred)
print (acc)


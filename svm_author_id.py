#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

from sklearn import svm
from sklearn.metrics import accuracy_score
       
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100]
 
#clf = svm.SVC(kernel = "linear") #Train using linear kernel
# tain using rbf kernel
clf = svm.SVC(C=10000.0,kernel = "rbf")

clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
#answer = pred[50]
#print answer
# TO find the accuracy
#accuracy = accuracy_score(labels_test,pred)
#print accuracy
no_test = len(pred)
sum = 0
for count in range(no_test):
    if(pred[count] == 1):
        sum +=1
print sum

#########################################################
### your code goes here ###

#########################################################



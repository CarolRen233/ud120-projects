#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
### use my own path 
sys.path.append("D:/yan/ML/ud120-projects/tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn import svm

clf=svm.SVC(kernel='rbf',C=10000,gamma='scale')

### if you want to have a faster training time, especially if you want to quikly test your code, you can minimize the traning size by the following way (remove"#"befor the code)

#features_train= features_train[:len(features_train)/100]
#labels_train= labels_train[:len(labels_train)/100] 

### training and training time
t0=time()
clf.fit(features_train,labels_train)
print "training time:",round(time()-t0,3),"s"

### predicting and predicting time
t0=time()
pred=clf.predict(features_test)
print "predicting time:",round(time()-t0,3),"s"

#count=0
#for i in pred:
    #if pred[i]==1:
	    
		#count+=1

#print count
	

### caculate accuracy
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(pred,labels_test)
print "accuracy:",accuracy



#########################################################



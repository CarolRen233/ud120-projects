#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

### pickle is from py3, when using py2, use cpickle
import cPickle as pickle
import sys
sys.path.append("D:/yan/ML/ud120-projects/tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("D:/yan/ML/ud120-projects/final_project/final_project_dataset.pkl", "rb") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]


sort_keys= pickle.load(open("D:/yan/ML/ud120-projects/tools/python2_lesson13_keys.pkl", "rb") )
data = featureFormat(data_dict, features_list, sort_keys)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!  

### split the data
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)


### creating decision tree
from sklearn import tree 
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)

### accuracy and fixing the reshaping problem

import numpy
from sklearn.metrics import accuracy_score

features_test=[features_test]

pred=clf.predict(numpy.array(features_test).reshape(-1,1))

accuracy=accuracy_score(pred,labels_test)
print "accuracy is:",accuracy


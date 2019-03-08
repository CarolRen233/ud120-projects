#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.

word_data = pickle.load( open("D:/yan/ML/ud120-projects/tools/word_data.pkl", "r"))
authors = pickle.load( open("D:/yan/ML/ud120-projects/tools/email_authors.pkl", "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()

### we need to know which feature has the largest importance score
feature_names = vectorizer.get_feature_names()

### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150]
labels_train   = labels_train[:150]



### your code goes here
### print the accuracy score when overfitting
from sklearn import tree  
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred=clf.predict(features_test)

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(labels_test,pred)
print "accuracy:",accuracy


### print a list of feature inportance,so we can see which feature is more important
fi=clf.feature_importances_

for index, feature, in enumerate(clf.feature_importances_):
    if feature>0.2:
        print "feature no", index
        print "importance", feature
        print "freature's name",feature_names[index]




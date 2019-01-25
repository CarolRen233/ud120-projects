#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("D:/yan/ML/ud120-projects/tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("D:/yan/ML/ud120-projects/final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL', 0 )
data = featureFormat(data_dict, features)



### your code below

### find the first outlier:
#max_value=sorted(data,reverse=True,key=lambda sal:sal[0])[0]
#print max_value

#for item in data_dict:
    #if data_dict[item]['salary']==max_value[0]:
	    #print item


### find the other 2 outliers, which bonus >5e6 and salary>1e6:
for item in data_dict:
    if data_dict[item]['bonus']!='NaN' and data_dict[item]['salary']!='NaN':
	    if data_dict[item]['bonus']>5e6 and data_dict[item]['salary']>1e6:
		    print item
			
	
		
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""



import pickle

enron_data = pickle.load(open("D:/yan/ML/ud120-projects/final_project/final_project_dataset.pkl", "r"))



### Q1:How many data points are in the Enron dataset? Answer:146
print "There are ",len(enron_data),"data points in this dataset"




### Q1:Print every key in the dictionary, which is the name of anron's manager in this case
print enron_data.keys()



### Q2:How many features in one key? Answer:21
print enron_data["METTS MARK"].values()  
count=0
for i in enron_data["METTS MARK"]:
    count+=1
print "There are ",count,"features in one key"




### Q3:How many POI(person of interest)in the Enron dataset? Answer:18
count=0
for i in enron_data.keys():
    if enron_data[i]["poi"]==1:
	    count+=1

print "There are ",count,"POI in this dataset"




### Q4:How many POI we listed? Answer:35
f= open('D:/yan/ML/ud120-projects/final_project/poi_names.txt')
context=f.readlines()

count=0
for line in context:
    if line.startswith('(y)')==True or line.startswith('(n)')==True:
	    count+=1
		
print "There are ",count,"POIs we listed"





### Q5: How much is James Prentice's total stock value? Answer:1095040
print enron_data["PRENTICE JAMES"].keys()
print "James Prentice's total stock value is",enron_data["PRENTICE JAMES"]["total_stock_value"]


### How many emails Wesley Colwell sent to poi?
print enron_data["COLWELL WESLEY"].keys()
print "There are ",enron_data["COLWELL WESLEY"]["from_this_person_to_poi"],"emails Wesley Colwell sent to poi"



### Q7: Who got the most money? How much money was it? Answer:Kenneth Lay,103559793

print "Jeffrey Skilling got",enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Kenneth Lay got",enron_data["LAY KENNETH L"]["total_payments"]
print "Andrew Fastow got",enron_data["FASTOW ANDREW S"]["total_payments"]




### How many folks in this dataset have a quantified salary and known email adress? Anwser:95 111
count1=0
count2=0
for key in enron_data:
    if enron_data[key]["salary"]!="NaN":
	    count1+=1
	
for key in enron_data:
	if enron_data[key]["email_address"]!="NaN":
	    count2+=1
		
print "There are ",count1,"folks in this dataset have a quantified salary"
print "There are ",count2,"folks in this dataset have a known email adress"


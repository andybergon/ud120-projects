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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print(enron_data)

print len(enron_data)

print len(enron_data['METTS MARK'])

count = 0
for name in enron_data:
    if enron_data[name]['poi'] == 1:
        count += 1
print 'poi', count

# count = 0
# for line in open('../final_project/poi_names.txt'):
#     if '(y)' in line.rstrip():
#         count += 1
# print count

count = 0
for line in open('../final_project/poi_names.txt'):
    if line.rstrip().startswith('('):
        count += 1
print count

print(enron_data['PRENTICE JAMES']['total_stock_value'])

print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])


print(enron_data['LAY KENNETH L']['total_payments'])
print(enron_data['SKILLING JEFFREY K']['total_payments'])
print(enron_data['FASTOW ANDREW S']['total_payments'])

salary_ok = 0
email_ok = 0
payments_ok = 0
payments_poi_ok = 0
for name in enron_data:
    sal = enron_data[name]['salary']
    if sal != 'NaN':
        salary_ok += 1
    if enron_data[name]['email_address'] != 'NaN':
        email_ok += 1
    if enron_data[name]['total_payments'] != 'NaN':
        payments_ok += 1
    if enron_data[name]['total_payments'] != 'NaN' and enron_data[name]['poi'] == 1:
        payments_poi_ok += 1
print salary_ok
print email_ok
print 'pay ok', payments_ok
print 'pay poi ok', payments_poi_ok
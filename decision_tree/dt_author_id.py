#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()



print len(features_train[0])
#########################################################
from sklearn import tree

clf = tree.DecisionTreeClassifier(min_samples_split=40)

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

score = clf.score(features_test, labels_test)

# print('[10]: {}, [26]: {}, [50]: {}'.format(clf.predict(features_test[10]),
#                                             clf.predict(features_test[26]),
#                                             clf.predict(features_test[50])))

# counter = 0
# for ft in features_test:
#     ft = np.array(ft).reshape(1,-1)
#     if clf.predict(ft) == 1:
#         counter += 1
#
# print counter

print score


#########################################################



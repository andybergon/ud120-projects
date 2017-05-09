#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


# #### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
# plt.show()

################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
from sklearn.neighbors import KNeighborsClassifier
clf1 = KNeighborsClassifier(n_neighbors=18, algorithm='auto')
clf1.fit(features_train, labels_train)
score1 = clf1.score(features_test, labels_test)
print score1


from sklearn.ensemble import AdaBoostClassifier
clf2 = AdaBoostClassifier(learning_rate=1.0)
clf2.fit(features_train, labels_train)
score2 = clf2.score(features_test, labels_test)
print score2


from sklearn.ensemble import RandomForestClassifier
clf3 = RandomForestClassifier(n_estimators=100)
clf3.fit(features_train, labels_train)
score3 = clf3.score(features_test, labels_test)
print score3


try:
    prettyPicture(clf1, features_test, labels_test)
    prettyPicture(clf2, features_test, labels_test)
    prettyPicture(clf3, features_test, labels_test)
except NameError:
    pass

# plt.show()

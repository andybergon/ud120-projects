#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""

import pickle
import sys

import matplotlib.pyplot as plt

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color=colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()


### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

### the input features we want to use
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = 'total_payments'
feature_4 = 'from_messages'
poi = "poi"
features_list = [poi, feature_1, feature_2, feature_3, feature_4]
data = featureFormat(data_dict, features_list)
poi, finance_features = targetFeatureSplit(data)


# calculate 'total_payments' max and min
def calculate_min_max(data_dict, feature_name):
    x = [v[feature_name] for k, v in data_dict.items() if v[feature_name] != 'NaN']
    return min(x), max(x)


print(calculate_min_max(data_dict, feature_2))
print(calculate_min_max(data_dict, feature_1))

# scale features
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(finance_features)
finance_features = scaler.transform(finance_features)

# scaled 'salary' and 'exercised_stock_options'
print(scaler.transform((200000, 1000000, 0, 0)))

# range of 'from_messages'
print(scaler.data_range[3])

# max_rescaled = [(x[0], x[1]) for x in finance_features if x[0] == max([y[0] for y in finance_features])]

### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2, _, _ in finance_features:
    plt.scatter(f1, f2)
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
from sklearn.cluster import KMeans

# use only 2 features
finance_features = [(x[0], x[1]) for x in finance_features]

clf = KMeans(n_clusters=2)
clf.fit(finance_features)
pred = clf.predict(finance_features)

### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"

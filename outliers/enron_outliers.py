#!/usr/bin/python

import pickle
import sys

import matplotlib.pyplot

sys.path.append("../tools/")
from feature_format import featureFormat

### read in data dictionary, convert to numpy array
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
features = ["salary", "bonus"]

# find and remove outlier
sorted_salary_and_bonus = sorted({k: (v['salary'], v['bonus']) for k, v in data_dict.items()}.items(),
                                 key=lambda xx: xx[1][0], reverse=True)
print(sorted_salary_and_bonus)
data_dict.pop('TOTAL', 0)

data = featureFormat(data_dict, features)

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

# Two people made bonuses of at least 5 million dollars, and a salary of over 1 million dollars
bandits = [x[0] for x in sorted_salary_and_bonus if
           (x[1][0] >= 1000000 and x[1][0] != 'NaN') and (x[1][1] >= 5000000 and x[1][1] != 'NaN')]
print(bandits)

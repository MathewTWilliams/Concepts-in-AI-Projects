import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestClassifier
from pathlib import PurePath, Path
# the following line allows ipython to display plots
# %matplotlib inline
csv_path = PurePath.joinpath(Path(__file__).resolve().parent, 
                    "cars.csv").as_posix()






"""`cars.csv` is in an easy-to-read comma separated format and the following 
*pandas* functionality makes it easy to read it into a `DataFrame` object. """

# read this csv file, remember to put the full path to 
# the directory where you saved the data
df = pd.read_csv(csv_path)  # df is DataFrame object
print (df.head())    # see the first 5 rows of the loaded table

print ("Data type: ") 
print (df.dtypes )

"""Scatterplot between MPG and Weight attributes:"""

plt.figure(figsize=(5,3))
plt.scatter(df['MPG'],df['Weight'], color='blue', alpha=0.2)
plt.xlabel("MPG")
plt.ylabel("weight")
plt.show()

'''
df.loc[df['Origin'] == 'Japan', 'label'] = 1  
df.loc[df['Origin'] == 'Europe', 'label'] = 2 
df.loc[df['Origin'] == 'US', 'label'] = 3 
print ( df['label'].value_counts(ascending=True) )
print ("Baseline accuracy: ")
print (254/(73+79+254))  # 0.62
# D tree is fine with this
'''

df.loc[df['Origin'] != 'US', 'label'] = int(0) 
df.loc[df['Origin'] == 'US', 'label'] = int(1)

data = df[['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 
'Acceleration', 'Model', 'label' ]]
X_train, X_test = train_test_split( data ,test_size=0.1, random_state=42)

train_bags   = X_train[ [ 'MPG', 'Cylinders','Horsepower', 'Weight', 'Model'] ]
train_labels =  X_train[ ['label'] ]

test_bags   = X_test[ [ 'MPG', 'Cylinders','Horsepower', 'Weight', 'Model'] ]
test_labels = X_test[ ['label'] ]

print (train_bags[:3])  # check first three data
print (train_labels[:3])  # check first three data

print ("Showing data labels: ")
print ( df['label'].value_counts(ascending=True) )

print ("Baseline accuracy: ")
print (254/(254+152))

print ("Model: Linear regression")
reg = LinearRegression()
reg.fit(train_bags, train_labels)
predictions = reg.predict( test_bags )
prediction_labels = [1 if x>0.7 else 0 for x in predictions ]
print ("Accuracy:" + str ( round( accuracy_score(test_labels, prediction_labels) , 
4) ) )

print ("*" * 25)
print ("Model: Decision Tree")
dTree = DecisionTreeClassifier( )         #max_depth= 5
dTree.fit(train_bags, train_labels)
predictions = dTree.predict(test_bags)
print ("Accuracy:" + str ( round( accuracy_score(test_labels, predictions) , 4) ) )


# Code added by Matt Williams
print("*" * 25)
print("Model: Linear Regression(w/ L1 regularization) ")
lasso_reg = Lasso()
lasso_reg.fit(train_bags, train_labels)
predictions = lasso_reg.predict(test_bags)
prediction_labels = [1 if x>0.7 else 0 for x in predictions]
print ("Accuracy:" + str ( round( accuracy_score(test_labels, prediction_labels) , 
4) ) )


print("*" * 25)
print("Model: Linear Regression(w/ L2 regularization) ")
ridge_reg = Ridge()
ridge_reg.fit(train_bags, train_labels)
predictions = ridge_reg.predict(test_bags)
prediction_labels = [1 if x>0.7 else 0 for x in predictions]
print ("Accuracy:" + str ( round( accuracy_score(test_labels, prediction_labels) , 
4) ) )


print("*" * 25)
print("Model: Random Forest")
rf_classifier = RandomForestClassifier()
rf_classifier.fit(train_bags, train_labels.values.ravel())
predictions = rf_classifier.predict(test_bags)
print ("Accuracy:" + str ( round( accuracy_score(test_labels, predictions) , 
4) ) )
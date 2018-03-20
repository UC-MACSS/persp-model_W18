# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:27:20 2018

@author: Riddhima Mishra
"""



cd C:\cygwin64\home\Riddhima Mishra\persp-model_W18\ProblemSets\PS4

import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import statsmodels.api as sm


#Question 1
#Q1 a
auto_data = pd.read_csv('Auto.csv')

#checking missing values

auto_data.isnull().sum()

#no missing values

print(auto_data.dtypes)

#horsepower is an object, converting it to float before regression 

auto_data['horsepower'] = pd.to_numeric(auto_data['horsepower'], errors='coerce')

#checking for Nas again

auto_data.isnull().sum()

#due to conversion to numeric, horsepower contains 5 NAs 

auto_data.dropna(inplace=True)


#Q1 b scatterplot

from pandas.plotting import scatter_matrix 
scatter_matrix(auto_data, alpha=0.3, figsize=(10, 10), diagonal= 'kde')
 

#Q1 c

#correlation matrix

df_subset = auto_data[['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'year', 'origin']]
df_subset.corr()

#Q1 d:  Estimating multiple linear regression

#defining a constant for B0

auto_data['const'] = 1

reg1 = sm.OLS(endog=auto_data['mpg'], exog=auto_data[['const', 'cylinders', 'horsepower', 'displacement', 'weight', 'acceleration','year', 'origin' ]], missing='drop')
type(reg1)


results= reg1.fit()
type(results)
print(results.summary())

# displacement, year and origin are significant at 1% level of significance

#cylinders, horsepower, acceleration

# Every year the mpg increases by 7.5% 

#(e)

#Based on the scatterplot matrix 3 variables that seem to have a non-linear relationship with
#mpg are: displacement, horsepower, weight, and acceleration 


#generating squared terms

auto_data['displacement_sqr'] = auto_data['displacement']**2
auto_data['horsepower_sqr'] = auto_data['horsepower']**2
auto_data['weight_sqr'] = auto_data['weight']**2
auto_data['acceleration_sqr'] = auto_data['acceleration']**2

reg2 = sm.OLS(endog=auto_data['mpg'], exog=auto_data[['const', 'cylinders','acceleration', 'acceleration_sqr', 'weight', 'weight_sqr','horsepower', 'horsepower_sqr', 'displacement', 'displacement_sqr','year', 'origin' ]], missing='drop')

type(reg2)


results= reg2.fit()
type(results)
print(results.summary())

#ii)

# New R-squared:                       0.870

# Old R-squared:                       0.821

#Better than the previous model


#iii)

#The coeffecient value changes direction and becomes insignificant, the squared coefficient is also insignificant and pretty small

#iv)

#significance value falls


#(f)

df_test = pd.DataFrame({
                        "constant" : [1],
                        "cylinders" : [6],
                        "displacement" : [200],
                        "displacement_sqr" : [200**2],
                        "horsepower" : [100],
                        "horsepower_sqr": [100**2],
                        "weight" : [3100],
                        "weight_sqr" : [3100**2],
                        "acceleration" : [15.1],
                        "acceleration_sqr" : [15.1**2],
                        "year" : [80],
                        "origin" : [1]
                        })


results.predict(df_test)

#Question 2 KNN 

#e)

df = pd.DataFrame({"x1"    :[0,2,0,0,-1,1],
                   "x2" : [3,0,1,1,0,1],
                   "x3"     :[ 0,0,3,2,1,1],
                   "y"   : ['Red', 'Red', 'Red', 'Green', 'Green', 'Red']})

#converting into numpy arrays

X = np.array(df.ix[:, 0:3]) 	# end index is exclusive
y = np.array(df['y']) 

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X, y)

df_new= pd.DataFrame({"x1" : [1],
                      "x2" : [1],
                      "x3" : [1]})

X_new = np.array(df_new.ix[:, 0:3]) 

print(knn.predict(X_new))

#Green
 

# Ques 3: Multivariable Logistic Regression


import sklearn
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics 
from sklearn.metrics import classification_report
from pylab import rcParams



auto_data = pd.read_csv('Auto.csv')
auto_data['horsepower'] = pd.to_numeric(auto_data['horsepower'], errors='coerce')

#this introduces 5 Null values
auto_data.dropna(inplace=True)
#Creating a dummy variable for mpg

auto_data['mpg_high'] = (auto_data['mpg'] >= auto_data['mpg'].median()).astype(int)
auto_data['const'] = 1

auto_data.info()


X = auto_data.ix[:, (1, 2, 3, 4, 5, 6, 7,10)].values
y = auto_data.ix[:, 9].values

logit_model=sm.Logit(y,X)
result=logit_model.fit()
print(result.summary())


#x4 (weight) and x 6 (year)

#b)

#Dividing the data into training and test

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5,
                                                    random_state=10)

#c)

logit_model=sm.Logit(y_train,X_train)
result_train=logit_model.fit()
print(result_train.summary())

#d: predicted values, confusion matrix, and classification report

#predicted values
from sklearn import metrics
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

#confusion matrix
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)

#classification report
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))




































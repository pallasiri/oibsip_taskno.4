# -*- coding: utf-8 -*-
"""CAR PRICE PREDICTION -OASIS

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cFjBgWYxp_Dwzlmm1B9TeSR8OpITP3RP

# **IMPORTING PACKAGES**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error

from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor

"""**READING THE FILE**"""

cdata=pd.read_csv("/content/drive/MyDrive/Colab Notebooks/DATASETS/CarPrice_Assignment.csv")

"""# **EXPLORATORY DATA ANALYSIS**

**1.UNDERSTANDING THE DATA**
"""

cdata.info()   #To check Null values and Feature Datatype

cdata.head()

"""**2.CLEANING THE DATA**"""

cdata=cdata.dropna()

cdata=cdata.drop_duplicates()

cdata.info()

enc=LabelEncoder()

for i in x.columns:
  if x[i].dtype == 'object':
    x[i] = enc.fit_transform(x[i])

cdata.fueltype = enc.fit_transform(cdata.fueltype)
cdata.aspiration =enc.fit_transform(cdata.aspiration)
cdata.doornumber =enc.fit_transform(cdata.doornumber)
cdata.carbody =enc.fit_transform(cdata.carbody)
cdata.drivewheel =enc.fit_transform(cdata.drivewheel)
cdata.enginelocation =enc.fit_transform(cdata.enginelocation)
cdata.enginetype =enc.fit_transform(cdata.enginetype)
cdata.cylindernumber =enc.fit_transform(cdata.cylindernumber)
cdata.fuelsystem =enc.fit_transform(cdata.fuelsystem)
cdata.CarName =enc.fit_transform(cdata.CarName)

""" **3. FEATURE SELECTION**"""

sns.histplot(cdata['price'])
plt.title('Distribution of Car Prices')
plt.xlabel('Price',color='white')
plt.ylabel('Count',color='white')
plt.style.use('dark_background')
sns.set_palette('dark')
plt.xticks(color='white')
plt.yticks(color='white')

cdata.info()

numeric_col=['wheelbase','carlength','carwidth','enginesize','boreratio','stroke','compressionratio','horsepower','peakrpm','citympg','highwaympg','price']
corr_matrix = cdata[numeric_col].corr()
sns.heatmap(corr_matrix)
sns.set_palette('dark')
plt.style.use('dark_background')
plt.show()

x = cdata.iloc[:,:25]
y = cdata['price']

x.head()

y.head()

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

model=LinearRegression()
model.fit(x_train,y_train)
y_predict=model.predict(x_test)
score=r2_score(y_test,y_predict)*100
score

model2=Ridge()  #alpha
model2.fit(x_train,y_train)
y_predict=model2.predict(x_test)
score2=r2_score(y_test,y_predict)*100
score2

model3=Lasso()
model3.fit(x_train,y_train)
y_predict=model3.predict(x_test)
score3=r2_score(y_test,y_predict)*100
score3

model4=SVR(kernel='linear', gamma=0.01) # linear,poly,sigmoid,rbf
model4.fit(x_train,y_train)
y_predict=model4.predict(x_test)
score4=r2_score(y_test,y_predict)*100
score4

model5=DecisionTreeRegressor()
model5.fit(x_train,y_train)
y_predict=model5.predict(x_test)
score5=r2_score(y_test,y_predict)*100
score5

model7=KNeighborsRegressor(n_neighbors=3)
model7.fit(x_train,y_train)
y_predict=model7.predict(x_test)
score7=r2_score(y_test,y_predict)*100
score7

"""# **CONCLUSION**

AS COMPARED TO ALL THE REGRESSOR MODELS DECISIONTREE REGRESSOR ODEL HAS GIVEN THE BEST ACCURACY WITH 90
...
HENCE DECISIONTREE REGRESSOR MODEL IS THE BEST MODEL FOR THE 'CAR PRICE PREDICTION DATASET'
"""
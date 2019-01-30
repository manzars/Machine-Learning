#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:35:32 2019

@author: manzars
"""
import pandas as pd
data = pd.read_csv("50_Startups.csv")
X = data.iloc[:, 0:4].values
y = data.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
lEncoder = LabelEncoder()
X[:, 3] = lEncoder.fit_transform(X[:, 3])
ohe = OneHotEncoder(categorical_features = [3])
X = ohe.fit_transform(X).toarray()

# to avoid dummy variable trap we always neglect one dummy variable but the function we are using for multi regression will take of that
# X = X[:, 1:] this will neglect first dummy variable

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)



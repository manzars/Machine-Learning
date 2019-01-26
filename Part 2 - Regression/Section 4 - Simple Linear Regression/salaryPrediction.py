#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 01:52:11 2019

@author: manzars
"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Salary_Data.csv")
X = data.iloc[:, 0:1].values
y = data.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 1/3, random_state = 42)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

plt.scatter(X_train, y_train, color = "red")
plt.plot(X_train, regressor.predict(X_train), color = "blue")
plt.title("Slary prediction")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()

plt.scatter(X_test, y_test, color = "red")
plt.plot(X_test, regressor.predict(X_test), color = "blue")
plt.title("Slary prediction")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()
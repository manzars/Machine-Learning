#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 17:51:02 2019

@author: manzars
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

data = pd.read_csv("Position_Salaries.csv")
X = data.iloc[:, 1:2].values
y = data.iloc[:, 2].values

regressor = LinearRegression()
regressor.fit(X, y)


poly_regressor = PolynomialFeatures(degree = 2)
X_poly = poly_regressor.fit_transform(X)

regressor2 = LinearRegression()
regressor2.fit(X_poly, y)

X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(-1,1)

plt.scatter(X, y, color = "red")
plt.plot(X_grid, regressor.predict(X_grid), color = "blue")
plt.title("Truth or Bluff")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()


plt.scatter(X, y, color = "red")
plt.plot(X_grid, regressor2.predict(poly_regressor.fit_transform(X_grid)), color = "blue")
# here we use poly_regressor cuz when we created the regressor for poly we pass there X_poly 
plt.title("Truth or Bluff")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()

# predicting the salary for position 6.5 using our 2 learning model

regressor.predict(np.array(6.5).reshape(-1,1)) # 330378.78787879 this much much more
regressor2.predict(poly_regressor.fit_transform(np.array(6.5).reshape(-1,1))) # 189498.10606061 this is pretty much accurate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 18:25:37 2019

@author: manzars
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("Position_Salaries.csv")
X = data.iloc[:, 1:2].values
y = data.iloc[:, 2].values


scaler_x = StandardScaler()
scaler_y = StandardScaler()
X = scaler_x.fit_transform(X)
y = scaler_y.fit_transform(y.reshape(-1,1))
y = y.reshape(len(y))

svr = SVR(kernel = "rbf")
svr.fit(X,y)

plt.scatter(X, y, color = "red")
plt.plot(X, svr.predict(X), color = "blue")
plt.show()

scaler_y.inverse_transform(svr.predict(scaler_x.transform(np.array(6.5).reshape(-1,1))))
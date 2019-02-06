#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 23:53:46 2019

@author: manzars
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Social_Network_Ads.csv")
X = data.iloc[:, 2:4].values
y = data.iloc[:, 4].values

from sklearn.preprocessing import StandardScaler
Scaler_X = StandardScaler()
X = Scaler_X.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(X_set[:, 0].min() -1, X_set[:, 0].max() +1, 0.01), np.arange(X_set[:, 1].min() -1, X_set[:, 1].max() +1, 0.01))

from matplotlib.colors import ListedColormap

plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), cmap = ListedColormap(('red', 'green')), alpha = 0.6)
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], color = ListedColormap(('red', 'green'))(i), label = j)
plt.title("K-NN")
plt.legend()
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.show()
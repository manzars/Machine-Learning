#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 20:58:48 2019

@author: manzars
"""
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd

data = pd.read_csv("train.csv")
plt.gray()
plt.matshow(X[33].reshape(28,28))
plt.show()

y = data.iloc[:, 0:1].values
X = data.iloc[:, 1:].values

classifier = RandomForestClassifier(n_estimators = 100, n_jobs = 3, criterion = "entropy", random_state = 0)
classifier.fit(X,y)
classifier.predict(X[33].reshape(1,784))

X_test = pd.read_csv("test.csv")
X_test = X_test.values
pred = classifier.predict(X)

cm = confusion_matrix(y, pred)


            
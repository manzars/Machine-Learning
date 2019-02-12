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

#loading the dataset of Digits of 8X8 matrix of gray scale
digit = load_digits()
data = digit.data
image = digit.images # this variable has 1797 8X8 matrix for pixel 
feature = digit.target # this variable has unique output

# Seperating 
X_train, X_test, y_train, y_test = train_test_split(data, feature, test_size = 0.25)
classifier = RandomForestClassifier(n_estimators = 100, criterion = "entropy", n_jobs = 3, random_state = 0)
classifier.fit(X_train, y_train)
pred = classifier.predict(X_test)
print("Predicted digit = {}".format(classifier.predict(digit.data[786].reshape(1,64))))
plt.gray()
plt.matshow(digit.images[786])
plt.show()
cm = confusion_matrix(y_test, pred)

from PIL import Image
img = np.asarray(Image.open('abc.jpg').convert('LA'))
img.save('greyscale.png')

import opencv

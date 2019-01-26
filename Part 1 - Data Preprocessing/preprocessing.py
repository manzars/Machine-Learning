import pandas as pd
import numpy as np
import matplotlib.pyplot as mlt

# Getting data

data = pd.read_csv("Data.csv")
X = data.iloc[:, 0:3].values
y = data.iloc[:, 3].values

# Filtering Data
# As there is blank value in dataset so we have to apply some function for make NaN value to saome mean, median, etc
# using Imputer of sklearn.preprocessing we can achive that

from sklearn.preprocessing import Imputer
imputer  = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

# As our dataset has some string value so we have to make that string value into some numerival value
# which is known as labelling

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 0] = labelencoder.fit_transform(X[:, 0])  #this will label each different value to some integer value
# but machine will judge those value in weight 

# so will use onehotencoder to make dummies value that can seperate each different value to an coloumn
ohe = OneHotEncoder(categorical_features = [0])
X = ohe.fit_transform(X).toarray()

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Now to make lerning model accurate we have to divide our data into training and test dataset


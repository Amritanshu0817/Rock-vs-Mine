# -*- coding: utf-8 -*-
"""Rock vs MIne.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RxOSdSRnfO2GSKBV7LG4LwZccw3kjeiO
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection and Data processing"""

#loading the dataset to a pandas Dataframe
sonar_data = pd.read_csv('/content/Copy of sonar data.csv', header = None)

sonar_data.head()

# number of rows and columns
sonar_data.shape

#describe = stastical measures of the data
sonar_data.describe()

sonar_data[60].value_counts()

sonar_data.groupby(60).mean()

#separating Data and Labels
X = sonar_data.drop(columns=60, axis=1)
Y = sonar_data[60]

print(X)
print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, stratify=Y, random_state=1)

print(X.shape, X_train.shape, X_test.shape)

print(X_train)
print(Y_train)

model = LogisticRegression()

#training the Logistic model with the training data
model.fit(X_train, Y_train)

"""Model Evaluation"""

#accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on training data : ', training_data_accuracy)

#accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on training data : ', training_data_accuracy)

"""Making a Predictive System

"""

input_data = (0.0363,0.0478,0.0298,0.0210,0.1409,0.1916,0.1349,0.1613,0.1703,0.1444,0.1989,0.2154,0.2863,0.3570,0.3980,0.4359,0.5334,0.6304,0.6995,0.7435,0.8379,0.8641,0.9014,0.9432,0.9536,1.0000,0.9547,0.9745,0.8962,0.7196,0.5462,0.3156,0.2525,0.1969,0.2189,0.1533,0.0711,0.1498,0.1755,0.2276,0.1322,0.1056,0.1973,0.1692,0.1881,0.1177,0.0779,0.0495,0.0492,0.0194,0.0250,0.0115,0.0190,0.0055,0.0096,0.0050,0.0066,0.0114,0.0073,0.0033)

#changing the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the np array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]=='R'):
  print('This is a Rock')
else:
    print('This is a Mine')
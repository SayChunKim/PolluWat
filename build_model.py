import numpy as np
import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import pickle

#read data
raw_data = pd.read_csv("Training_Set.csv")
data = raw_data.dropna(axis=1) #drop missing values

#identify features and classes
features = ['Carbon','Nitrogen','Phosphorus']
labels = ["Chicken","Cabbage"]
X = data[features]
y = data[labels]

#build model
model = RandomForestClassifier(random_state=1)
model.fit(X,y)

#save the model to disk
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))
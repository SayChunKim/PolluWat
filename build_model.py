import numpy as np
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
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
print(model.score(X,y))
#save the model to disk
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))
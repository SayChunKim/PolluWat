import numpy as np
import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

#read data
raw_data = pd.read_csv("Training_Set.csv")
data = raw_data.dropna(axis=1) #drop missing values

#identify features and classes
features = ['Carbon','Nitrogen','Phosphorus']
labels = ["Chicken","Cabbage"]
X = data[features]
y = data[labels]
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

#build model
#model1 = LogisticRegression(random_state=1)
model2 = RandomForestClassifier(random_state=1)
#model3 = LinearSVC(random_state=1)
#model1.fit(train_X,train_y)
model2.fit(train_X,train_y)
#model3.fit(train_X,train_y)

#test model
#predictions1 = model1.predict(val_X)
predictions2 = model2.predict(val_X)
#redictions3 = model3.predict(val_X)
#mae1 = mean_absolute_error(predictions1, val_y)
mae2 = mean_absolute_error(predictions2, val_y)
#mae3 = mean_absolute_error(predictions3, val_y)
print(mae2)

# save the model to disk
#filename = 'finalized_model.sav'
#pickle.dump(model, open(filename, 'wb'))
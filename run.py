import numpy as np
import pandas as pd 
import pickle
import requests
import json
from sklearn.ensemble import RandomForestClassifier

#load the model
model = 'finalized_model.sav'
loaded_model = pickle.load(open(model,'rb'))

#load the input data
url = ['http://api-m2x.att.com/v2/devices/311acec855cc5d3a3e3572eae55fce4f/streams',
'http://api-m2x.att.com/v2/devices/fce1aa4b1021ff6f410019e926cba437/streams',
'http://api-m2x.att.com/v2/devices/c1771604215f182808353fd24a061cdf/streams',
'http://api-m2x.att.com/v2/devices/ad92e743c28b50af1f53d22e5ccfac06/streams',
'http://api-m2x.att.com/v2/devices/a26bcc6e79924b31a6053daa675fb7f5/streams']
api = ['8a904b5dd863af3f2e3397b175940dc6',
'abbde49d0c005030e488ce4d48b83fef',
'f742c703e511cd94e75611840432a78c',
'f136db58faec0ddd79fe08f6c661ad6f',
'c9e05d8a0967e1608fff6037c51ac433']
device = ['sgMyDD1','sgMyDD2','sgMyDD3','sgMyDD4','sgMyDD5']

values = []
for i in range(len(url)):
    r = requests.get(url[i],headers={'X-M2X-KEY':api[i]})
    content = r.json()
    first = content['streams'][0]
    row = [first['created'],device[i]]
    for con in content['streams']:
        row.append(con['value'])
    values.append(row)

#create dataframe
df = pd.DataFrame(np.array(values), columns = ['Time','Device','Carbon','Nitrogen','Phosphorus'])
print(df.head())
features = ['Carbon','Nitrogen','Phosphorus']
X = df[features]

#make predictions
predictions = loaded_model.predict_proba(X)
df[''] = predictions

#export to json
output = result.to_json()
with open('data.txt', 'w') as outfile:  
    json.dump(output, outfile)
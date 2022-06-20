# Importing the libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv('classification.csv')

y = data[["success"]]
x = data.drop(columns=["success"])
rf = RandomForestClassifier(random_state=123)
rf.fit(x,y)

pickle.dump(rf, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[22.573729142097473, 17.96922325097786]]))
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

#load data
df= pd.read_csv(r'S:\IIHMR-B\Advanced Analytics 2\cicd_pipeline\data\data.csv')

X=df[["area","bedrooms"]]
y=df["price"]

#train model
model= LinearRegression()
model.fit(X,y)

#save model
with open(r'S:\IIHMR-B\Advanced Analytics 2\cicd_pipeline\backend\models\model.pkl','wb') as f:
    pickle.dump(model,f)
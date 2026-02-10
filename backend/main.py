from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import pickle
import numpy as np

app = FastAPI (title="Linear Regression API")

#import os
#MODEL PATH = Path(os.getenv("MODEL_PATH", "models/model.pkl"))

# MODEL_PATH = r"S:\IIHMR-B\Advanced Analytics 2\cicd_pipeline\backend\models\model.pkl"
MODEL_PATH = Path(os.getenv("MODEL_PATH", "models/model.pkl"))
try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load model from {MODEL_PATH}: {e}")

class InputData(BaseModel):
    area: float
    bedrooms: int

@app.get("/")
def healt_check():
    return {"status": "API running"}

@app.post("/predict")
def predict(data: InputData):
    X = np.array([[data.area, data.bedrooms]])
    prediction = model.predict(X)[0]
    return {"Predicted_price": float(prediction)}    
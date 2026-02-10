import pytest
from fastapi.testclient import TestClient
from pathlib import Path
import os
import pickle
import numpy as np

#Import your app (adjust if you rename it)
from backend.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "API running"}

def test_predict_valid_input():
    payload = {
        "area": 1500.0,
        "bedrooms": 3}
    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "Predicted_price" in data 
    assert isinstance(data["Predicted_price"], (int, float))
    assert data["Predicted_price"] > 0  #assuming house price should be positive

    
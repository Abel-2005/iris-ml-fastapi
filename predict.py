from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Create FastAPI app
app = FastAPI(title="Iris Prediction API")

# Input schema
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Home route
@app.get("/")
def home():
    return {"message": "Iris Prediction API is running"}

# Prediction route
@app.post("/predict")
def predict(data: IrisInput):
    features = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    prediction = model.predict(features)[0]

    return {"prediction": int(prediction)}

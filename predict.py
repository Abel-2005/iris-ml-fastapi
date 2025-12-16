from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np


with open("model.pkl", "rb") as f:
    model = pickle.load(f)


app = FastAPI(title="Iris Prediction API")


class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/")
def home():
    return {"message": "Iris Prediction API is running"}


@app.post("/predict")
def predict(data: IrisInput):
    input_data = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    prediction = model.predict(input_data)[0]

    return {"prediction": int(prediction)}

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("../models/landslide_model.pkl")
le = joblib.load("../models/label_encoder.pkl")

@app.get("/")
def home():
    return {"message": "AI API is running"}

@app.post("/predict")
def predict(data: dict):
    rainfall = data["rainfall"]
    slope = data["slope"]
    soil = data["soil_type"]

    soil_encoded = le.transform([soil])[0]

    X = pd.DataFrame([[rainfall, slope, soil_encoded]],
                     columns=["rainfall", "slope", "soil_type"])

    prediction = model.predict(X)[0]

    if prediction == 1:
        result = "HIGH RISK"
    else:
        result = "LOW RISK"

    return {"prediction": result}
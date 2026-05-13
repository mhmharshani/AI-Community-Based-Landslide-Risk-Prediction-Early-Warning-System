from datetime import datetime

from fastapi import HTTPException
import pandas as pd

from app.ml_models.predictor import make_prediction

def predict_landslide(data):

    try:
        prediction, confidence = make_prediction(data)

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Prediction failed"
        )

    risk = "HIGH RISK" if prediction == 1 else "LOW RISK"
   
    print("Prediction request:", data)
    print("Prediction result:", risk)
    return {
        "prediction": risk,
        "confidence": confidence,
        "predicted_at": datetime.now()
    }
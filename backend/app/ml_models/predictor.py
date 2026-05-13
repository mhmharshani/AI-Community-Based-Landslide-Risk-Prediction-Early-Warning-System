import pandas as pd

from app.ml_models.model_loader import model, encoder

def make_prediction(data):

    soil_encoded = encoder.transform([data.soil_type])[0]

    X = pd.DataFrame(
        [[data.rainfall, data.slope, soil_encoded]],
        columns=["rainfall", "slope", "soil_type"]
    )

    prediction = model.predict(X)[0]
    
    probability = model.predict_proba(X)[0]

    confidence = round(max(probability) * 100, 2)

    return prediction, confidence


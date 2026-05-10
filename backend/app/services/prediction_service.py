import pandas as pd

from app.ml_models.model_loader import model, encoder

def predict_landslide(data):

    soil_encoded = encoder.transform([data.soil_type])[0]

    X = pd.DataFrame(
        [[data.rainfall, data.slope, soil_encoded]],
        columns=["rainfall", "slope", "soil_type"]
    )

    prediction = model.predict(X)[0]

    if prediction == 1:
        return "HIGH RISK"

    return "LOW RISK"


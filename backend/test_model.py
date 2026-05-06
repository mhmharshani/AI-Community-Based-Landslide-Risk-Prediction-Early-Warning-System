import joblib
import pandas as pd

model = joblib.load("../models/landslide_model.pkl")
le = joblib.load("../models/label_encoder.pkl")

rainfall = 150
slope = 40
soil = "clay"

soil_encoded = le.transform([soil])[0]

X = pd.DataFrame([[rainfall, slope, soil_encoded]],
                 columns=["rainfall", "slope", "soil_type"])

prediction = model.predict(X)

if prediction[0] == 1:
    print("HIGH RISK: Landslide likely")
else:
    print("LOW RISK: Safe")
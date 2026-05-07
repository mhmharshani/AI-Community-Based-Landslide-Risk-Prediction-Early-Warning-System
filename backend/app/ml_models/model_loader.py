import joblib

model = joblib.load("app/ml_models/landslide_model.pkl")
encoder = joblib.load("app/ml_models/label_encoder.pkl")
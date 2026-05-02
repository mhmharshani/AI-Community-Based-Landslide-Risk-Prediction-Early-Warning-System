import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

data = pd.read_csv("../data/dataset.csv")

le = LabelEncoder()
data["soil_type"] = le.fit_transform(data["soil_type"])

X = data[["rainfall", "slope", "soil_type"]]
y = data["landslide"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "../models/landslide_model.pkl")
joblib.dump(le, "../models/label_encoder.pkl")

print("Model trained and saved successfully!")
from pydantic import BaseModel

class PredictionRequest(BaseModel):
    rainfall: float
    slope: float
    soil_type: str
from fastapi import APIRouter

from app.dto.prediction_request import PredictionRequest
from app.services.prediction_service import predict_landslide

router = APIRouter()

@router.post("/predict")
def predict(data: PredictionRequest):

    result = predict_landslide(data)

    return{
        "message": "Prediction completed successfully",
        "Prediction data": result
    }

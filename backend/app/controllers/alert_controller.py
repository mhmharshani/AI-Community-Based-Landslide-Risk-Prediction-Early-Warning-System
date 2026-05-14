
from fastapi import APIRouter

from app.dto.alert_request import AlertRequest
from app.services.alert_service import create_alert


router = APIRouter()

@router.post("/alert")
def add_alert(data: AlertRequest):
    
    result = create_alert(data, "MANUAL")

    return {
        "Alert Response": result
    }
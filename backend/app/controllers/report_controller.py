
from fastapi import APIRouter

from app.dto.report_request import ReportRequest
from app.services.report_service import create_report


router = APIRouter()

@router.post("/report")
def add_report(data: ReportRequest):
    print("Received report data: ", data)
    
    result = create_report(data)

    return {
        "Community Report": result
    }


from fastapi import APIRouter

from app.dto.report_request import ReportRequest
from app.services.report_service import save_report


router = APIRouter()

@router.post("/report")
def create_report(data: ReportRequest):

    result = save_report(data)

    return {
        "report": result
    }
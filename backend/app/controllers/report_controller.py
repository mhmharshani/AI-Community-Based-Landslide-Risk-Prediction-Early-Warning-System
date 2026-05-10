
from fastapi import APIRouter

from app.dto.report_request import ReportRequest
from app.services.report_service import create_report, fetch_report_by_id, get_all_reports


router = APIRouter()

@router.post("/report")
def add_report(data: ReportRequest):
    print("Received report data: ", data)
    
    result = create_report(data)

    return {
        "Community Report": result
    }

@router.get("/all-reports")
def get_reports():
    
    result = get_all_reports()
    return {
        "All Reports": result
    }

@router.get("/report/{id}")
def get_report_by_id(id: str):

    result = fetch_report_by_id(id)
    return {
        "Report": result                   
    }

from fastapi import APIRouter

from app.dto.report_request import ReportRequest
from app.services.report_service import create_report, delete_report_by_id, fetch_report_by_id, filter_reports, get_all_reports


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
        "Report with id": result                   
    }

@router.delete("/delete-report/{id}")
def delete_report(id: str):
    result = delete_report_by_id(id)
    return {
        "Deleted Report": result
    }

@router.get("/reports")
def filter_reports_by_risk(risk: str=None):
    result = filter_reports(risk)
    return {        
        "Reports filtered by risk": result
    }
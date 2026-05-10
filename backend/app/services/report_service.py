import uuid

from app.repositories.report_repository import find_report_by_id, find_reports, save_report

def create_report(data):

    report_id = str(uuid.uuid4())

    report = {
        "id": report_id,
        "location": data.location,
        "observations": data.observations,
        "description": data.description,
        "media_urls": data.media_urls,
        "risk": data.risk
    }

    print("In Service - Report:", report)

    saved_result = save_report(report)

    return {
        "message": "Report saved successfully",
        "report_id": saved_result["id"]
    }

def get_all_reports():

    all_reports = find_reports()
    return all_reports

def fetch_report_by_id(id):
    report = find_report_by_id (id)

    if report==None:
        return {
            "message": "Report not found"
        }
    else : 
        return report
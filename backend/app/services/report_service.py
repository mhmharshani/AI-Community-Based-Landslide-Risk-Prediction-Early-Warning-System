import uuid

from app.repositories.report_repository import save_report

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
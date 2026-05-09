import uuid

def save_report(data):

    report_id = str(uuid.uuid4())

    report = {
        "id": report_id,
        "location": data.location,
        "observations": data.observations,
        "description": data.description,
        "media_urls": data.media_urls,
        "risk": data.risk
    }

    print(report)
    print(type(report))

    return {
        "message": "Report submitted successfully",
        "report_id": report["id"]
    }
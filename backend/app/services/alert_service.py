
from datetime import datetime
from uuid import UUID


def create_alert(alert,source):

    alert_response = {
        "id": UUID,
        "location": alert.location,
        "message": alert.message,
        "severity": alert.severity,
        "source": source,
        "prediction_confidence": alert.prediction_confidence,
        "created_at": datetime.now(),
        "is_active": True,
        "is_deleted": False
    }

    return alert_response
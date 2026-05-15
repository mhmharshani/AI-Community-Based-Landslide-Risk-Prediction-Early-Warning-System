
from datetime import datetime
from uuid import UUID
import uuid

from app.repositories.alert_repository import save_alert


def create_alert(alert,source):

    alert_response = {
        "id": str(uuid.uuid4()),
        "location": alert.location,
        "message": alert.message,
        "severity": alert.severity,
        "source": source,
        "created_at": datetime.now().isoformat(),
        "is_active": True,
        "is_deleted": False
    }

    saved_alert_response = save_alert(alert_response)

    return saved_alert_response
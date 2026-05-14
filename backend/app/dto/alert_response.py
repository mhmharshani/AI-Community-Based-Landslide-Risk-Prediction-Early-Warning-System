
from pydantic import BaseModel

from app.dto.alert_source import AlertSource


class AlertResponse(BaseModel):
    id: str
    location: str
    message: str
    severity: str
    source: AlertSource
    prediction_confidence: float
    created_at: str
    is_active: bool
    is_deleted: bool
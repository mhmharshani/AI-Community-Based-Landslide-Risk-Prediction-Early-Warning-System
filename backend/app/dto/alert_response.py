
import uuid

from pydantic import BaseModel, Field

from app.dto.alert_source import AlertSource


class AlertResponse(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    location: str
    message: str
    severity: str
    source: AlertSource
    prediction_confidence: float
    created_at: str
    is_active: bool
    is_deleted: bool
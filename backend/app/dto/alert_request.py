
from pydantic import BaseModel


class AlertRequest(BaseModel):
    location: str
    message: str
    severity: str
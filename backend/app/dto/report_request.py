from pydantic import BaseModel

from app.dto.risk_level import RiskLevel

class ReportRequest(BaseModel):
    location: str
    observations: list[str]
    description: str
    media_urls : list[str] = []
    risk: RiskLevel
    is_deleted: bool = False
   